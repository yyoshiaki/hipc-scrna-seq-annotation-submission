# v15 cluster-consensus annotation summary

## 実行方針

v15 は、旧 final label を土台にしない cluster-consensus annotation として実行しました。入力は以下に限定しています。

- full-gene portal H5AD
- neutral source-evidence container
- generic marker registry
- official ontology

cell-level marker winner は直接 final label にせず、Leiden/subcluster 単位で source support、marker score、negative/confound marker、doublet/QC を集約しました。CD4 T Effector Memory は、cluster 全体を rescue する条件は満たさなかったため、reference >=2 かつ marker support があり、CD8/NK signal が優位でない limited subset のみ rescue しています。

## Clean execution check

v15 関連の default inputs は neutral 名にしました。

```text
configs/manifest.tsv
configs/marker_registry.yaml
outputs/final_annotations/260602_current_evidence/evidence/*.evidence.h5ad
```

`scripts/260602_build_v15_cluster_consensus.py` は旧 final label column を読みません。`v13/v14` の文字列は、出力に混入した場合に止める validation check にだけ残っています。

すべての v15 H5AD は以下を満たしました。

- full-gene var space を保持
- `X_umap` あり
- `submission_cell_type` と submission TSV の一致
- obs column/value に `v13`, `v14`, `version` なし

## Summary

| study | cells | genes | labels | parent/Blood fraction | doublets | CD4 TEM |
|---|---:|---:|---:|---:|---:|---:|
| infection_study_01 | 54,924 | 33,538 | 22 | 8.8% | 1,278 | 1,159 |
| infection_study_04 | 43,767 | 26,361 | 23 | 8.0% | 132 | 53 |
| vaccination_study_04 | 66,065 | 16,983 | 17 | 2.0% | 647 | 0 |
| vaccination_study_06 | 57,419 | 11,878 | 19 | 13.8% | 1,502 | 445 |
| vaccination_study_09 | 139,960 | 19,141 | 20 | 7.1% | 579 | 865 |

## vaccination_study_09 T cell interpretation

`vaccination_study_09` では、marker-only CD4 TEM は 7,667 cells でしたが、v15 では 865 cells に抑制されました。これは、CD4 TEM marker が CD8/MAIT/NK-like cytotoxic program と混ざって過大に出るためです。

v15 の CD4 TEM はすべて `limited_subset_reference_marker_support` 由来です。つまり、大きな Leiden cluster を丸ごと CD4 TEM にしたわけではなく、mixed cluster 内で reference と marker が両方支持する細胞だけを拾っています。

## Outputs

```text
outputs/final_annotations/260602_v15_cluster_consensus/submissions/
outputs/final_annotations/260602_v15_cluster_consensus/cellxgene/
outputs/final_annotations/260602_v15_cluster_consensus/tables/
```

Key tables:

```text
outputs/final_annotations/260602_v15_cluster_consensus/tables/final_annotation_summary_cluster_consensus.tsv
outputs/final_annotations/260602_v15_cluster_consensus/tables/final_annotation_label_counts_cluster_consensus.tsv
outputs/final_annotations/260602_v15_cluster_consensus/tables/cluster_consensus_decisions.tsv
```

## Current assessment

v15 は v14 より clean で、T cell marker winner の過剰 rescue は抑えられています。一方で、parent/Blood Cell が一部増えており、特に `vaccination_study_06` はまだ conservative です。次に見るべき点は、Blood Cell fallback の内訳と、T/NK lineage の cluster-level parent fallback が biologically reasonable かどうかです。
