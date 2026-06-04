# HIPC データセットアノテーションレポート: {{REPORT_TITLE}}

更新日: {{REPORT_UPDATED}}

このレポートは `hipc-annotation` Codex workflow によって生成したデータセット別レビュー文書です。固定 method は repository README に置き、このレポートでは実際の evidence、弱い箇所、レビュー優先度、UMAP / dotplot を確認します。

## データセット概要

{{STUDY_SUMMARY_TABLE}}

## 実行概要

{{RUN_SUMMARY}}

## データセット固有の解釈

{{INTERPRETATION_NOTES}}

## データセット固有の評価

{{DATASET_ASSESSMENT}}

## Marker Gene 欠損アラート

{{MARKER_ALERTS}}

## ソース間不一致

{{SOURCE_DISAGREEMENT}}

## レビュー優先事項

{{REVIEW_CONCERNS}}

## ラベル構成

{{LABEL_COMPOSITION}}

## Inline Figures

{{FIGURE_BLOCKS}}

## Subcluster Marker Score Review

上の lineage-specific panel は、各 lineage subset で HVG 選択、PCA、neighbors、Leiden、UMAP を再計算した true local subcluster analysis から生成しています。Marker gene による fine label の確認は global UMAP だけではなく、この local UMAP、CellTypist/Azimuth/Pan-human/cluster-level marker gene assignment overlay、cluster marker gate score UMAP、marker-expression UMAP、dotplot を主に見ます。Treg など sparse marker label は cell-wise marker winner ではなく、local cluster の FOXP3/IL2RA/CTLA4 など key-marker support と reference support で判定します。

## Marker Assignment Feedback

Marker gene assignment は final label を強制的に上書きするものではなく、cluster-level の自己点検です。この表は marker-only assignment と final/reference-driven label がずれる cluster、marker specificity が弱い cluster、scRefMap が期待される lineage で欠落する cluster を示します。`marker_score` は raw marker base score から negative/confound marker penalty を差し引いた cluster-level marker gate score です。

{{MARKER_FEEDBACK_TABLE}}

## Cluster Consensus Evidence

{{SUBCLUSTER_EVIDENCE_TABLE}}

## 出力ファイル

{{FILE_BLOCK}}
