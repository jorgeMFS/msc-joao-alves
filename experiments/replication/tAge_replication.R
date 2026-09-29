# 1. Python 
Sys.setenv(RETICULATE_PYTHON = "C:/Users/João Alves/AppData/Local/Programs/Python/Python314/python.exe")

# 2. Packages
library(tAge)
library(readxl)
library(Biobase)

# 3. Dados 
exprs_data <- read.csv("C:/Users/João Alves/Desktop/Thesis/msc-joao-alves/data/raw/Expression_data_absolute_rodents_Scaled.csv",
                       row.names = 1, check.names = FALSE)

metadata <- as.data.frame(read_excel("C:/Users/João Alves/Desktop/Thesis/msc-joao-alves/results/table_Zenodo.xlsx"))
rownames(metadata) <- as.character(metadata[[1]])

# 4. Amostras comuns 
comuns <- intersect(colnames(exprs_data), rownames(metadata))
stopifnot(length(comuns) == 161)
exprs_data <- exprs_data[, comuns]
metadata <- metadata[comuns, ]

# 5. ExpressionSet
eset <- make_ExpressionSet(exprs_data, metadata)

# 6. Alinhar com a lista de genes e control_subtraction, por grupo
gene_list <- tAge:::load_gene_list()
grupos <- unique(as.character(metadata$Group))

por_grupo <- lapply(grupos, function(g) {
  e <- eset[, metadata$Group == g]
  e <- tAge:::.align_to_gene_list(e, gene_list)
  tAge:::control_subtraction(e, column_name = "Intervention",
                             control_label = "Control", verbose = TRUE)
})

eset_diff <- tAge:::.tage_cbind_esets(por_grupo, sample_order = colnames(eset))
eset_diff <- tAge:::.tage_set_species(eset_diff, species = "mouse")
tAge_eset <- list(scaled_diff = eset_diff)

todos <- list.files(pasta_modelos, pattern = "\\.pkl$", full.names = TRUE)

# 7. Um modelo de cada vez (o nome da coluna sai igual em todos, por isso guardo à parte)
previsoes <- lapply(todos, function(f) {
  tryCatch({
    r <- predict_tAge(tAge_eset, list(scaled_diff = f), mode = "EN")
    col <- grep("EN_tAge$", colnames(r), value = TRUE)[1]
    setNames(r[[col]], r$Sample)
  }, error = function(e) {
    message("Falhou: ", basename(f), " -> ", conditionMessage(e))
    NULL
  })
})
names(previsoes) <- gsub("^EN_|_scaleddiff\\.pkl$", "", basename(todos))
previsoes <- previsoes[!sapply(previsoes, is.null)]

# 8. Tabela: metadados originais + uma coluna por modelo
tabela <- metadata
for (nm in names(previsoes)) {
  tabela[[paste0("pred_", nm)]] <- previsoes[[nm]][rownames(tabela)]
}

# 9. Colunas de diferença (previsto - valor de referência do teu ficheiro)
refs <- c(
  Mortality_Rodents_Liver        = "Expected_Hazard.log10",
  Mortality_Mouse_Multitissue    = "Expected_Hazard.log10",
  Mortality_Rodents_Multitissue  = "Expected_Hazard.log10"
)
for (nm in intersect(names(refs), names(previsoes))) {
  tabela[[paste0("dif_", nm)]] <- tabela[[paste0("pred_", nm)]] - tabela[[refs[nm]]]
}

# 10. Verificação rápida
for (nm in intersect(names(refs), names(previsoes))) {
  cat(nm, "| correlação:", round(cor(tabela[[paste0("pred_", nm)]], tabela[[refs[nm]]], use = "complete.obs"), 3),
      "| diferença média absoluta:", round(mean(abs(tabela[[paste0("dif_", nm)]]), na.rm = TRUE), 3), "\n")
}

write.csv(tabela, "C:/Users/João Alves/Desktop/Thesis/msc-joao-alves/results/comparacao_tAge_figado.csv", row.names = FALSE)