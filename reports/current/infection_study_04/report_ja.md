# infection_study_04 提出レポート

Updated: 2026-06-12 11:49:00 EDT

このレポートは、2026-06-12締切用のTeam04 emergency submission TSVから直接生成しています。古いv22診断UMAP画像は含めていません。

## 提出ファイル

- TSV: `submission_package_emergency_260612.zip` 内の `submissions/infection_study_04_annotation.tsv`
- このdatasetで使ったsource package: `v22` (reviewed v22 evidence)
- 行数: 43,767
- template行数: 43,767
- barcode順序がtemplateと一致: `True`
- 提出label数: 15
- confidence中央値: 0.7762
- low-confidence cell数: 497

## Validation

- 列名OK: `True`
- invalid ontology label数: 0
- confidence範囲: 0.4500 to 0.8500

## 解釈

このdatasetは、label diversityが高く、barcode/order/ontology validationを通過したv22 evidence由来TSVを使っています。

## Label Counts

| predicted_cell_type | n_cells | fraction |
| --- | --- | --- |
| Classical Monocyte | 11458 | 0.262 |
| CD4 Naive / T Central Memory | 8829 | 0.202 |
| CD8 Cytotoxic / T Effector Memory | 7788 | 0.178 |
| NK Cell | 6433 | 0.147 |
| Plasma Cell | 3150 | 0.072 |
| Naive B Cell | 2126 | 0.049 |
| Memory B Cell | 1344 | 0.031 |
| Non-Classical Monocyte | 1214 | 0.028 |
| Blood Cell | 436 | 0.010 |
| Conventional DC 2 | 338 | 0.008 |
| Plasmacytoid DC | 229 | 0.005 |
| Neutrophil | 195 | 0.004 |
| Platelet | 86 | 0.002 |
| HSC | 80 | 0.002 |
| Doublet | 61 | 0.001 |

完全なlabel count表: `tables/final_submission_label_counts.tsv`
