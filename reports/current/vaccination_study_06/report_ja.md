# vaccination_study_06 提出レポート

Updated: 2026-06-12 11:49:00 EDT

このレポートは、2026-06-12締切用のTeam04 emergency submission TSVから直接生成しています。古いv22診断UMAP画像は含めていません。

## 提出ファイル

- TSV: `submission_package_emergency_260612.zip` 内の `submissions/vaccination_study_06_annotation.tsv`
- このdatasetで使ったsource package: `v22` (reviewed v22 evidence)
- 行数: 57,419
- template行数: 57,419
- barcode順序がtemplateと一致: `True`
- 提出label数: 12
- confidence中央値: 0.7724
- low-confidence cell数: 3,430

## Validation

- 列名OK: `True`
- invalid ontology label数: 0
- confidence範囲: 0.3870 to 0.8500

## 解釈

このdatasetは、label diversityが高く、barcode/order/ontology validationを通過したv22 evidence由来TSVを使っています。

## Label Counts

| predicted_cell_type | n_cells | fraction |
| --- | --- | --- |
| CD4 Naive / T Central Memory | 29818 | 0.519 |
| CD8 Cytotoxic / T Effector Memory | 10013 | 0.174 |
| NK Cell | 9877 | 0.172 |
| Memory B Cell | 2547 | 0.044 |
| Doublet | 2162 | 0.038 |
| MAIT Cell | 1538 | 0.027 |
| Blood Cell | 746 | 0.013 |
| Myeloid Cell | 468 | 0.008 |
| Naive B Cell | 175 | 0.003 |
| Non-Classical Monocyte | 54 | 0.001 |
| Intermediate Monocyte | 20 | 0.000 |
| B Cell | 1 | 0.000 |

完全なlabel count表: `tables/final_submission_label_counts.tsv`
