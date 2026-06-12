# infection_study_03 提出レポート

Updated: 2026-06-12 11:49:00 EDT

このレポートは、2026-06-12締切用のTeam04 emergency submission TSVから直接生成しています。古いv22診断UMAP画像は含めていません。

## 提出ファイル

- TSV: `submission_package_emergency_260612.zip` 内の `submissions/infection_study_03_annotation.tsv`
- このdatasetで使ったsource package: `current_clean` (current_clean fallback)
- 行数: 646,739
- template行数: 646,739
- barcode順序がtemplateと一致: `True`
- 提出label数: 4
- confidence中央値: 0.4437
- low-confidence cell数: 646,739

## Validation

- 列名OK: `True`
- invalid ontology label数: 0
- confidence範囲: 0.3847 to 0.5432

## 解釈

このdatasetは、締切前により良いclean evidence由来TSVが用意できなかったため、current_clean fallback TSVを使っています。label粒度は保守的に解釈してください。

## Label Counts

| predicted_cell_type | n_cells | fraction |
| --- | --- | --- |
| Blood Cell | 215411 | 0.333 |
| T Cell | 200576 | 0.310 |
| Myeloid Cell | 137478 | 0.213 |
| B Cell | 93274 | 0.144 |

完全なlabel count表: `tables/final_submission_label_counts.tsv`
