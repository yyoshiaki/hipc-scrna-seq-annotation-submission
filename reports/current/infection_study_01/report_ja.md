# infection_study_01 提出レポート

Updated: 2026-06-12 11:49:00 EDT

このレポートは、2026-06-12締切用のTeam04 emergency submission TSVから直接生成しています。古いv22診断UMAP画像は含めていません。

## 提出ファイル

- TSV: `submission_package_emergency_260612.zip` 内の `submissions/infection_study_01_annotation.tsv`
- このdatasetで使ったsource package: `v22` (reviewed v22 evidence)
- 行数: 54,924
- template行数: 54,924
- barcode順序がtemplateと一致: `True`
- 提出label数: 16
- confidence中央値: 0.7772
- low-confidence cell数: 2,527

## Validation

- 列名OK: `True`
- invalid ontology label数: 0
- confidence範囲: 0.4500 to 0.8500

## 解釈

このdatasetは、label diversityが高く、barcode/order/ontology validationを通過したv22 evidence由来TSVを使っています。

## Label Counts

| predicted_cell_type | n_cells | fraction |
| --- | --- | --- |
| Classical Monocyte | 17789 | 0.324 |
| CD8 Cytotoxic / T Effector Memory | 10509 | 0.191 |
| NK Cell | 8060 | 0.147 |
| CD4 T Effector Memory | 4387 | 0.080 |
| Naive B Cell | 4269 | 0.078 |
| CD4 Naive / T Central Memory | 2341 | 0.043 |
| Memory B Cell | 2100 | 0.038 |
| Non-Classical Monocyte | 1979 | 0.036 |
| Platelet | 1313 | 0.024 |
| Doublet | 981 | 0.018 |
| Conventional DC 2 | 469 | 0.009 |
| MAIT Cell | 284 | 0.005 |
| Blood Cell | 178 | 0.003 |
| Plasma Cell | 128 | 0.002 |
| Plasmacytoid DC | 93 | 0.002 |
| Plasmablast | 44 | 0.001 |

完全なlabel count表: `tables/final_submission_label_counts.tsv`
