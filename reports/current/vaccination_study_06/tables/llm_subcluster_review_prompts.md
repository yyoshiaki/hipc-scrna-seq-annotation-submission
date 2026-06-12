# LLM Subcluster Review Queue

Use these packets as a review layer. Do not directly mutate per-cell labels. Return dataset-specific concerns, ontology-gap hypotheses, and general policy updates to test in the deterministic pipeline.

## vaccination_study_06 Myeloid_lineage cluster 1

- Priority: high (7)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=1; cells=58; final=Myeloid Cell; marker_assignment=Intermediate Monocyte; raw_marker_winner=Intermediate Monocyte; assignment_reason=raw_marker_winner; marker_score=0.616; best_total_score=0.616; score_margin=0.049; CellTypist=CD4 Naive / T Central Memory:32; CD4 T Effector Memory:16; B Cell:5; Treg:1; T Cell:1; PanHuman=Blood Cell:23; CD4 Naive / T Central Memory:13; CD4 T Cell (ab):8; Treg:5; Memory B Cell:4; scRefMap=CD4 Naive / T Central Memory:47; Treg:3; not_available:3; Memory B Cell:3; Naive B Cell:2; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final,low_total_score_or_margin.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 Myeloid_lineage cluster 6

- Priority: high (7)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=6; cells=45; final=Myeloid Cell; marker_assignment=Intermediate Monocyte; raw_marker_winner=Intermediate Monocyte; assignment_reason=raw_marker_winner; marker_score=0.550; best_total_score=0.550; score_margin=0.116; CellTypist=CD4 Naive / T Central Memory:37; CD8 Cytotoxic / T Effector Memory:2; Naive B Cell:2; CD4 T Effector Memory:2; Memory B Cell:1; PanHuman=Blood Cell:19; CD4 Naive / T Central Memory:13; Treg:5; CD4 T Effector Memory:5; CD4 T Cell (ab):2; scRefMap=CD4 Naive / T Central Memory:31; not_available:8; Treg:4; CD4 T Effector Memory:1; Naive B Cell:1; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final,low_total_score_or_margin.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 3

- Priority: medium (6)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=3; cells=3230; final=CD8 Cytotoxic / T Effector Memory; marker_assignment=CD8 Cytotoxic / T Effector Memory; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.664; best_total_score=2.948; score_margin=2.223; CellTypist=CD8 Cytotoxic / T Effector Memory:3083; NK Cell:82; CD4 T Effector Memory:46; MAIT Cell:17; CD4 Naive / T Central Memory:1; PanHuman=CD8 Cytotoxic / T Effector Memory:2165; Blood Cell:493; NK Cell:319; gdT Cell:97; CD8 T Cell (ab):81; scRefMap=not_available:3191; CD4 T Effector Memory:35; CD4 Naive / T Central Memory:3; Treg:1; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 5

- Priority: medium (6)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=5; cells=3181; final=NK Cell; marker_assignment=NK Cell; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.921; best_total_score=3.364; score_margin=2.443; CellTypist=NK Cell:2990; CD8 Cytotoxic / T Effector Memory:190; MAIT Cell:1; PanHuman=NK Cell:2502; Blood Cell:358; T Cell:265; CD8 Cytotoxic / T Effector Memory:44; CD8 T Cell (ab):10; scRefMap=not_available:3181; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 6

- Priority: medium (6)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=6; cells=2915; final=NK Cell; marker_assignment=NK Cell; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.860; best_total_score=3.118; score_margin=2.099; CellTypist=NK Cell:2472; CD8 Cytotoxic / T Effector Memory:404; MAIT Cell:24; CD4 Naive / T Central Memory:14; B Cell:1; PanHuman=NK Cell:1087; Blood Cell:937; T Cell:552; CD8 Cytotoxic / T Effector Memory:230; gdT Cell:28; scRefMap=not_available:2861; CD4 T Effector Memory:41; CD4 Naive / T Central Memory:13; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 14

- Priority: medium (6)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=14; cells=2123; final=NK Cell; marker_assignment=NK Cell; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.916; best_total_score=3.162; score_margin=1.656; CellTypist=NK Cell:1190; CD8 Cytotoxic / T Effector Memory:798; gdT Cell:132; MAIT Cell:2; T Cell:1; PanHuman=NK Cell:1749; Blood Cell:189; T Cell:86; CD8 Cytotoxic / T Effector Memory:77; CD8 T Cell (ab):17; scRefMap=not_available:2121; CD4 Naive / T Central Memory:1; CD4 T Effector Memory:1; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 15

- Priority: medium (6)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=15; cells=1538; final=MAIT Cell; marker_assignment=MAIT Cell; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.778; best_total_score=2.590; score_margin=1.387; CellTypist=MAIT Cell:1046; CD8 Cytotoxic / T Effector Memory:338; CD4 T Effector Memory:138; NK Cell:11; CD4 Naive / T Central Memory:4; PanHuman=MAIT Cell:476; Blood Cell:342; CD4 T Cell (ab):296; CD8 Cytotoxic / T Effector Memory:188; gdT Cell:102; scRefMap=not_available:1380; CD4 T Effector Memory:97; CD4 Naive / T Central Memory:59; Treg:2; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 16

- Priority: medium (6)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=16; cells=1460; final=NK Cell; marker_assignment=NK Cell; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.848; best_total_score=2.907; score_margin=1.683; CellTypist=NK Cell:1169; CD8 Cytotoxic / T Effector Memory:278; gdT Cell:11; CD4 Naive / T Central Memory:2; PanHuman=NK Cell:526; Blood Cell:426; CD8 Cytotoxic / T Effector Memory:220; T Cell:210; CD8 T Cell (ab):49; scRefMap=not_available:1431; CD4 T Effector Memory:26; CD4 Naive / T Central Memory:3; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 Myeloid_lineage cluster 7

- Priority: medium (6)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=7; cells=39; final=Myeloid Cell; marker_assignment=Intermediate Monocyte; raw_marker_winner=Intermediate Monocyte; assignment_reason=raw_marker_winner; marker_score=0.954; best_total_score=0.954; score_margin=0.231; CellTypist=Memory B Cell:38; CD8 Cytotoxic / T Effector Memory:1; PanHuman=Blood Cell:27; Memory B Cell:5; T Cell:4; B Cell:1; Treg:1; scRefMap=not_available:24; CD4 Naive / T Central Memory:7; Treg:4; Memory B Cell:2; Naive B Cell:2; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 Myeloid_lineage cluster 9

- Priority: medium (6)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=9; cells=35; final=Myeloid Cell; marker_assignment=Conventional DC 2; raw_marker_winner=Conventional DC 2; assignment_reason=raw_marker_winner; marker_score=0.581; best_total_score=0.959; score_margin=0.378; CellTypist=NK Cell:22; CD8 Cytotoxic / T Effector Memory:10; gdT Cell:1; CD4 Naive / T Central Memory:1; Memory B Cell:1; PanHuman=Blood Cell:27; NK Cell:5; T Cell:1; CD8 Cytotoxic / T Effector Memory:1; Memory B Cell:1; scRefMap=not_available:32; CD4 T Effector Memory:2; Naive B Cell:1; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 2

- Priority: medium (5)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=2; cells=3407; final=CD4 Naive / T Central Memory; marker_assignment=CD4 Naive / T Central Memory; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.314; best_total_score=3.317; score_margin=2.947; CellTypist=CD4 Naive / T Central Memory:3049; CD8 Cytotoxic / T Effector Memory:147; Treg:63; NK Cell:59; MAIT Cell:52; PanHuman=CD4 Naive / T Central Memory:1236; Blood Cell:936; Treg:373; T Cell:267; CD4 T Cell (ab):254; scRefMap=CD4 Naive / T Central Memory:2000; not_available:1024; CD4 T Effector Memory:293; Treg:90; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 7

- Priority: medium (5)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=7; cells=2893; final=CD4 Naive / T Central Memory; marker_assignment=CD4 Naive / T Central Memory; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.319; best_total_score=3.338; score_margin=2.577; CellTypist=CD4 Naive / T Central Memory:2531; CD8 Cytotoxic / T Effector Memory:118; CD4 T Effector Memory:103; MAIT Cell:65; Treg:61; PanHuman=Blood Cell:624; CD4 T Effector Memory:582; Treg:566; CD4 T Cell (ab):462; CD4 Naive / T Central Memory:435; scRefMap=CD4 Naive / T Central Memory:1867; not_available:526; CD4 T Effector Memory:388; Treg:112; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 18

- Priority: medium (5)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=18; cells=894; final=CD8 Cytotoxic / T Effector Memory; marker_assignment=CD8 Cytotoxic / T Effector Memory; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.582; best_total_score=3.077; score_margin=2.496; CellTypist=CD8 Cytotoxic / T Effector Memory:890; NK Cell:4; PanHuman=CD8 Cytotoxic / T Effector Memory:677; Blood Cell:120; CD8 T Cell (ab):54; NK Cell:39; T Cell:2; scRefMap=not_available:894; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 Myeloid_lineage cluster 0

- Priority: medium (5)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=0; cells=83; final=Myeloid Cell; marker_assignment=Intermediate Monocyte; raw_marker_winner=Intermediate Monocyte; assignment_reason=raw_marker_winner; marker_score=1.000; best_total_score=1.000; score_margin=0.276; CellTypist=B Cell:38; Memory B Cell:33; Naive B Cell:11; CD4 Naive / T Central Memory:1; PanHuman=Memory B Cell:79; Blood Cell:4; scRefMap=Naive B Cell:51; Memory B Cell:28; not_available:3; CD4 Naive / T Central Memory:1; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 Myeloid_lineage cluster 2

- Priority: medium (5)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=2; cells=57; final=Myeloid Cell; marker_assignment=Intermediate Monocyte; raw_marker_winner=Intermediate Monocyte; assignment_reason=raw_marker_winner; marker_score=0.897; best_total_score=0.897; score_margin=0.113; CellTypist=Memory B Cell:21; CD4 Naive / T Central Memory:19; B Cell:13; Naive B Cell:2; CD8 Cytotoxic / T Effector Memory:2; PanHuman=Blood Cell:32; Memory B Cell:22; CD4 T Cell (ab):1; Platelet:1; T Cell:1; scRefMap=Naive B Cell:20; not_available:19; CD4 Naive / T Central Memory:7; CD4 T Effector Memory:5; Treg:4; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 Myeloid_lineage cluster 3

- Priority: medium (5)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=3; cells=55; final=Myeloid Cell; marker_assignment=Intermediate Monocyte; raw_marker_winner=Intermediate Monocyte; assignment_reason=raw_marker_winner; marker_score=0.872; best_total_score=0.872; score_margin=0.159; CellTypist=Memory B Cell:32; B Cell:14; CD4 Naive / T Central Memory:4; NK Cell:3; CD8 Cytotoxic / T Effector Memory:1; PanHuman=Memory B Cell:31; Blood Cell:20; CD4 T Effector Memory:1; Plasma Cell:1; Treg:1; scRefMap=Naive B Cell:21; not_available:13; Memory B Cell:12; CD4 Naive / T Central Memory:5; Treg:3; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 Myeloid_lineage cluster 5

- Priority: medium (5)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=5; cells=47; final=Myeloid Cell; marker_assignment=Intermediate Monocyte; raw_marker_winner=Intermediate Monocyte; assignment_reason=raw_marker_winner; marker_score=0.939; best_total_score=0.939; score_margin=0.148; CellTypist=B Cell:31; Memory B Cell:12; Naive B Cell:4; PanHuman=Memory B Cell:41; Blood Cell:5; B Cell:1; scRefMap=Naive B Cell:28; Memory B Cell:13; not_available:4; Plasma Cell:2; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 Myeloid_lineage cluster 8

- Priority: medium (5)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=8; cells=38; final=Myeloid Cell; marker_assignment=Intermediate Monocyte; raw_marker_winner=Intermediate Monocyte; assignment_reason=raw_marker_winner; marker_score=0.957; best_total_score=0.957; score_margin=0.306; CellTypist=B Cell:37; Memory B Cell:1; PanHuman=Memory B Cell:36; CD8 Cytotoxic / T Effector Memory:1; Blood Cell:1; scRefMap=Naive B Cell:19; Memory B Cell:18; not_available:1; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 Myeloid_lineage cluster 11

- Priority: medium (5)
- Suggested action: check_if_finer_official_label_is_supported
- Evidence packet: Study=vaccination_study_06; lineage=Myeloid_lineage; cluster=11; cells=11; final=Myeloid Cell; marker_assignment=Intermediate Monocyte; raw_marker_winner=Intermediate Monocyte; assignment_reason=raw_marker_winner; marker_score=1.000; best_total_score=1.000; score_margin=0.466; CellTypist=B Cell:7; Memory B Cell:2; CD4 Naive / T Central Memory:1; Naive B Cell:1; PanHuman=Memory B Cell:10; Blood Cell:1; scRefMap=Naive B Cell:7; Plasma Cell:2; CD4 Naive / T Central Memory:1; Memory B Cell:1; review_reasons=parent_or_broad_final_label,marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 19

- Priority: medium (4)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=19; cells=270; final=CD4 Naive / T Central Memory; marker_assignment=Treg; raw_marker_winner=Treg; assignment_reason=raw_marker_winner; marker_score=0.519; best_total_score=2.609; score_margin=1.081; CellTypist=CD4 Naive / T Central Memory:87; CD8 Cytotoxic / T Effector Memory:86; Treg:79; NK Cell:10; MAIT Cell:3; PanHuman=Blood Cell:65; CD4 T Cell (ab):61; Treg:55; T Cell:24; NK Cell:22; scRefMap=CD4 Naive / T Central Memory:125; not_available:99; CD4 T Effector Memory:27; Treg:19; review_reasons=marker_assignment_disagrees_with_final,ambiguous_or_missing_label_candidate.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 T_NK_lineage cluster 20

- Priority: medium (4)
- Suggested action: evaluate_ontology_gap_or_conservative_policy
- Evidence packet: Study=vaccination_study_06; lineage=T_NK_lineage; cluster=20; cells=160; final=NK Cell; marker_assignment=NK Cell; raw_marker_winner=NKT Cell; assignment_reason=conservative_policy_blocks_raw_marker_winner; marker_score=0.952; best_total_score=3.367; score_margin=2.416; CellTypist=NK Cell:150; CD8 Cytotoxic / T Effector Memory:10; PanHuman=NK Cell:93; T Cell:27; Blood Cell:26; CD8 Cytotoxic / T Effector Memory:12; CD4 Naive / T Central Memory:1; scRefMap=not_available:159; CD4 T Effector Memory:1; review_reasons=raw_marker_winner_changed_by_policy,ambiguous_or_missing_label_candidate,screfmapping_not_available.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 B_lineage cluster 1

- Priority: low (2)
- Suggested action: review_marker_vs_reference_disagreement
- Evidence packet: Study=vaccination_study_06; lineage=B_lineage; cluster=1; cells=211; final=Memory B Cell; marker_assignment=Naive B Cell; raw_marker_winner=Naive B Cell; assignment_reason=raw_marker_winner; marker_score=0.769; best_total_score=3.032; score_margin=1.527; CellTypist=Memory B Cell:132; B Cell:76; Naive B Cell:3; PanHuman=Memory B Cell:211; scRefMap=Naive B Cell:123; Memory B Cell:76; Plasma Cell:12; review_reasons=marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 B_lineage cluster 2

- Priority: low (2)
- Suggested action: review_marker_vs_reference_disagreement
- Evidence packet: Study=vaccination_study_06; lineage=B_lineage; cluster=2; cells=179; final=Memory B Cell; marker_assignment=Naive B Cell; raw_marker_winner=Naive B Cell; assignment_reason=raw_marker_winner; marker_score=0.163; best_total_score=2.590; score_margin=1.533; CellTypist=B Cell:117; Memory B Cell:58; CD4 Naive / T Central Memory:2; CD8 Cytotoxic / T Effector Memory:1; Naive B Cell:1; PanHuman=Memory B Cell:147; Blood Cell:23; B Cell:3; Treg:2; Plasma Cell:1; scRefMap=Naive B Cell:129; Memory B Cell:37; not_available:7; Plasma Cell:4; CD4 T Effector Memory:1; review_reasons=marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 B_lineage cluster 5

- Priority: low (2)
- Suggested action: review_marker_vs_reference_disagreement
- Evidence packet: Study=vaccination_study_06; lineage=B_lineage; cluster=5; cells=173; final=Memory B Cell; marker_assignment=Naive B Cell; raw_marker_winner=Naive B Cell; assignment_reason=raw_marker_winner; marker_score=0.218; best_total_score=3.173; score_margin=2.407; CellTypist=B Cell:173; PanHuman=Memory B Cell:172; Blood Cell:1; scRefMap=Memory B Cell:84; Naive B Cell:79; Plasma Cell:10; review_reasons=marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 B_lineage cluster 6

- Priority: low (2)
- Suggested action: review_marker_vs_reference_disagreement
- Evidence packet: Study=vaccination_study_06; lineage=B_lineage; cluster=6; cells=165; final=Memory B Cell; marker_assignment=Naive B Cell; raw_marker_winner=Naive B Cell; assignment_reason=raw_marker_winner; marker_score=0.084; best_total_score=2.628; score_margin=1.647; CellTypist=Memory B Cell:81; B Cell:80; CD4 Naive / T Central Memory:2; CD8 Cytotoxic / T Effector Memory:1; Naive B Cell:1; PanHuman=Memory B Cell:137; Blood Cell:20; Plasma Cell:3; B Cell:2; Platelet:1; scRefMap=Naive B Cell:119; Memory B Cell:29; not_available:8; Plasma Cell:6; CD4 Naive / T Central Memory:2; review_reasons=marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 B_lineage cluster 7

- Priority: low (2)
- Suggested action: review_marker_vs_reference_disagreement
- Evidence packet: Study=vaccination_study_06; lineage=B_lineage; cluster=7; cells=144; final=Memory B Cell; marker_assignment=Naive B Cell; raw_marker_winner=Naive B Cell; assignment_reason=raw_marker_winner; marker_score=0.129; best_total_score=2.889; score_margin=2.082; CellTypist=Memory B Cell:75; B Cell:62; CD4 Naive / T Central Memory:3; NK Cell:2; CD8 Cytotoxic / T Effector Memory:1; PanHuman=Memory B Cell:131; Blood Cell:10; Plasma Cell:1; Naive B Cell:1; CD4 T Cell (ab):1; scRefMap=Naive B Cell:77; Memory B Cell:53; Plasma Cell:6; not_available:5; CD4 Naive / T Central Memory:2; review_reasons=marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 B_lineage cluster 8

- Priority: low (2)
- Suggested action: review_marker_vs_reference_disagreement
- Evidence packet: Study=vaccination_study_06; lineage=B_lineage; cluster=8; cells=141; final=Memory B Cell; marker_assignment=Naive B Cell; raw_marker_winner=Naive B Cell; assignment_reason=raw_marker_winner; marker_score=0.293; best_total_score=2.850; score_margin=1.422; CellTypist=B Cell:88; Memory B Cell:31; Naive B Cell:20; CD4 Naive / T Central Memory:2; PanHuman=Memory B Cell:127; Blood Cell:12; CD4 T Cell (ab):1; CD4 Naive / T Central Memory:1; scRefMap=Naive B Cell:90; Memory B Cell:39; Plasma Cell:4; not_available:3; CD4 Naive / T Central Memory:3; review_reasons=marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 B_lineage cluster 9

- Priority: low (2)
- Suggested action: review_marker_vs_reference_disagreement
- Evidence packet: Study=vaccination_study_06; lineage=B_lineage; cluster=9; cells=135; final=Memory B Cell; marker_assignment=Naive B Cell; raw_marker_winner=Naive B Cell; assignment_reason=raw_marker_winner; marker_score=0.114; best_total_score=2.785; score_margin=1.948; CellTypist=B Cell:99; Memory B Cell:33; CD4 Naive / T Central Memory:2; Naive B Cell:1; PanHuman=Memory B Cell:118; Blood Cell:9; B Cell:4; Plasma Cell:2; Naive B Cell:1; scRefMap=Naive B Cell:77; Memory B Cell:42; Plasma Cell:11; not_available:4; CD4 Naive / T Central Memory:1; review_reasons=marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 B_lineage cluster 10

- Priority: low (2)
- Suggested action: review_marker_vs_reference_disagreement
- Evidence packet: Study=vaccination_study_06; lineage=B_lineage; cluster=10; cells=133; final=Memory B Cell; marker_assignment=Naive B Cell; raw_marker_winner=Naive B Cell; assignment_reason=raw_marker_winner; marker_score=0.086; best_total_score=2.758; score_margin=2.103; CellTypist=Memory B Cell:127; B Cell:3; NK Cell:2; CD4 Naive / T Central Memory:1; PanHuman=Memory B Cell:125; Blood Cell:6; HSC:1; B Cell:1; scRefMap=Naive B Cell:63; Plasma Cell:40; Memory B Cell:24; not_available:5; CD4 Naive / T Central Memory:1; review_reasons=marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?

## vaccination_study_06 B_lineage cluster 11

- Priority: low (2)
- Suggested action: review_marker_vs_reference_disagreement
- Evidence packet: Study=vaccination_study_06; lineage=B_lineage; cluster=11; cells=133; final=Memory B Cell; marker_assignment=Naive B Cell; raw_marker_winner=Naive B Cell; assignment_reason=raw_marker_winner; marker_score=0.847; best_total_score=2.756; score_margin=0.812; CellTypist=B Cell:128; Naive B Cell:4; Memory B Cell:1; PanHuman=Memory B Cell:131; Blood Cell:2; scRefMap=Naive B Cell:113; Memory B Cell:20; review_reasons=marker_assignment_disagrees_with_final.

Review question: Is the final official label appropriate, is this an ontology-gap case, or should a general registry/policy update be tested?
