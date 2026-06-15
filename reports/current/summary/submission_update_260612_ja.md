# HIPC 提出候補アップデート 2026-06-12

更新日: 2026-06-12 EDT

## 結論

現時点の緊急提出候補は `submission_package_v24_pragmatic_260612.zip` です。

この package は以下の混合方針です。

- `infection_study_01`, `infection_study_04`, `vaccination_study_04`, `vaccination_study_06`, `vaccination_study_09`: 既に安定していた v22 output を使用。
- `infection_study_03`, `infection_study_06`, `vaccination_study_01`: specificity を少し上げるため v23 aggressive marker rescue output を使用。
- `vaccination_study_10`: transformed 1271-gene input で marker-only rescue が危険なため v24 safe fallback を使用。
- `infection_study_07`: raw count 不足により organizer guidance に従って提出対象から除外。

## 提出候補 package

共有サーバー上の zip:

`/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_package_v24_pragmatic_260612.zip`

比較用:

- Safe: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_package_v24_safe_260612.zip`
- Aggressive: `/vast/palmer/pi/hafler/yy693/HIPC-scRNAseq-Annotation/outputs/submission_package_v23_aggressive_260612.zip`

## 重要な注意

v23 は marker-only rescue により parent/Blood label を減らせますが、marker availability alert と label-specific conservative gate を迂回する危険がありました。v24 ではこの問題を修正しました。

ただし v24 safe は安全側に倒れすぎ、`infection_study_03`, `infection_study_06`, `vaccination_study_01`, `vaccination_study_10` で parent/Blood label が多く残ります。そのため緊急提出用には pragmatic package を作成しました。

## Summary Tables

- [Pragmatic package summary](tables/submission_package_v24_pragmatic_260612_summary.tsv)
- [Safe package summary](tables/submission_package_v24_safe_260612_summary.tsv)
- [Aggressive package summary](tables/submission_package_v23_aggressive_260612_summary.tsv)

## Detailed Reports for Review

submission 前に UMAP 上で確認すべき 4 dataset の detailed report です。

- [infection_study_03 Japanese](../infection_study_03/report_ja.md), [English](../infection_study_03/report_en.md)
- [infection_study_06 Japanese](../infection_study_06/report_ja.md), [English](../infection_study_06/report_en.md)
- [vaccination_study_01 Japanese](../vaccination_study_01/report_ja.md), [English](../vaccination_study_01/report_en.md)
- [vaccination_study_10 Japanese](../vaccination_study_10/report_ja.md), [English](../vaccination_study_10/report_en.md)
