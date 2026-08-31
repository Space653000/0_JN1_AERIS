# 0_JN1_AERIS

**AERIS — Acoustic Engineering & Research Intelligence System**

本 repository 用於建立一套可長期保存、模型可替換、證據可追溯、工程結果可驗證的 AI 聲學工程組織系統。

## Web UI — 2026-08-31

AERIS 第一版固定三個主要入口：

1. [Dashboard / Mission Control](index.html)  
   AERIS 全域狀態、100-seat Role Library、Acoustic Autonomous R&D Loop、Evidence / Trust North-Star KPI。

2. [Engineering Workspace](workspace.html)  
   Human Chief Engineer 的單一工作入口；輸入產品、工程問題、風險與證據需求，由 AERIS 動態組建 Temporary Engineering Pod。

3. [Service Console](services.html)  
   Control / Knowledge / Execution / Trust / Operations 五個 backend planes；Verification G0–G5、Risk R0–R4、Evidence Bundle、Health semantics。

> **重要：**目前三頁為 Target-state static prototype。任何 `HEALTHY` / 完成狀態在未連接真實 telemetry、Evidence 與 Verification backend 前，都不得視為正式工程事實。

## 2026-08-31 Research / Architecture Baseline

1. [AERIS Master Research & Architecture Baseline](docs/research/AERIS_MASTER_RESEARCH_ARCHITECTURE_BASELINE_20260831.md)  
   主 RFC：AERIS × Kairos、AI-native organization、Speaker/Microphone 六大專業、100 Virtual Engineering Seats、Evidence / Verification / Reproducibility、Standards Intelligence、P0–P3 Roadmap。

2. [AERIS Research Data Index](docs/research/AERIS_RESEARCH_DATA_INDEX_20260831.md)  
   研究數據索引：把 SOURCE-FACT、SYNTHESIS、AERIS-DECISION、TARGET、VERIFY-LATER 分開，保留量化數據、標準狀態、工具、角色與來源 URL。

3. [Kairos / LifeOS Deep Research](docs/research/2026-08-31_Kairos_LifeOS_AERIS_Deep_Research.md)  
   Kairos Agent Harness、Memory、Skills、Workflow、事故、Evidence-before-Done、Human Approval 與 AERIS 可移植設計。

4. [AERIS Web UI / Control Plane Baseline](docs/research/AERIS_WEB_UI_CONTROL_PLANE_BASELINE_20260831.md)  
   補足三個正式 Web 入口、Dashboard truth semantics、Temporary Pod UX、Service Console、Benchmark 100 與 UI/Backend 分工。

## Core Architecture

> **1 Human Chief Engineer + 100 Virtual Acoustic Engineering Seats + model-neutral orchestration + real engineering tools + Evidence + Independent Verification + Human Approval + Reproducibility.**

100 seats are capabilities, not 100 always-running agents. Typical active pod size is **2–8 roles**, or **5–15 roles** for complex work.

## North Star

> **AERIS is not an AI-agent demo. It is an Acoustic Engineering Organization OS whose engineering conclusions remain traceable, verifiable and reproducible even after today’s models are replaced.**
