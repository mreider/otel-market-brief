# Lesser-Known Observability, OTel, and AI Observability Startups

Research compiled April 2, 2026. Excludes Dash0, Chronosphere, Honeycomb, SigNoz, Groundcover, Cribl, Arize AI, and Braintrust (already covered).

---

## Part 1: OTel-Native and Infrastructure Observability

### Odigos
- **What they do:** Open-source observability control plane that automates OpenTelemetry instrumentation using eBPF. Zero-code distributed tracing for Kubernetes environments.
- **Founded:** 2022/2023 (sources vary), Tel Aviv, Israel. Founders: Ari Recht (CEO), Eden Federman (CTO). Originally called Keyval.
- **Funding:** $13M Series A (September 2024), led by Venture Guides, with Salesforce Ventures, Mango Capital, Firestreak Ventures. Notable angels: Martin Mao (Chronosphere CEO), Christine Yen (Honeycomb CEO), Ben Sigelman (Lightstep/OTel co-creator). YC W23 alum.
- **OTel relationship:** Core contributor to the OTel eBPF Instrumentation SIG (launched May 2025), alongside Grafana Labs, Splunk, and Coralogix. Maintains the Go auto-instrumentation eBPF repo.
- **Key differentiation:** Only company that is both a commercial product and a major contributor to the OTel eBPF spec itself. Zero-code tracing for any language via eBPF protocol-level instrumentation.
- **Why they matter:** Their eBPF instrumentation approach is being standardized into OpenTelemetry itself via the OBI (OpenTelemetry eBPF Instrumentation) project. If OBI becomes the default way to instrument, Odigos is deeply embedded in that standard.
- Sources: [TechCrunch](https://techcrunch.com/2024/09/09/yc-alum-odigos-aims-to-help-enterprises-find-errors-and-stamp-out-latency-in-their-systems/), [VentureGuides](https://www.ventureguides.com/news/odigos-raises-13m-in-funding-to-revolutionize-application-performance-tracing), [OTel OBI docs](https://opentelemetry.io/docs/zero-code/obi/)

---

### Coroot
- **What they do:** Open-source observability and APM with AI-powered root cause analysis. eBPF-based, zero-instrumentation monitoring for Kubernetes and VMs.
- **Founded:** September 2021, Palo Alto, CA. Founders: Anton Petruhin, Peter Zaitsev (Percona founder), Nikolay Sivko.
- **Funding:** No external funding disclosed. Bootstrapped / self-funded by co-founder Peter Zaitsev (who sold Percona).
- **OTel relationship:** OpenTelemetry-compatible for ingesting traces and metrics. Uses eBPF for auto-instrumentation rather than OTel SDKs, but feeds data into OTel-compatible pipelines.
- **Key differentiation:** Predefined inspections that identify root causes for 80%+ of issues without configuration. Apache 2.0 licensed. Combines metrics, logs, traces, continuous profiling, and SLO-based alerting out of the box. Recently extended beyond K8s to VMs/bare-metal.
- **Why they matter:** The "Percona of observability" play -- Peter Zaitsev built Percona as the open-source MySQL company. Same playbook here: build the best open-source alternative, then monetize via enterprise support and managed services. No VC pressure means they can play the long game.
- Sources: [GitHub](https://github.com/coroot/coroot), [InfoQ](https://www.infoq.com/news/2024/05/coroot-apm-observability/), [Help Net Security](https://www.helpnetsecurity.com/2026/02/23/coroot-open-source-observability-apm-tool/)

---

### Metoro
- **What they do:** Kubernetes-native AI SRE platform. Combines full-stack telemetry (metrics, logs, traces, profiling) with an AI assistant called Guardian for automated issue detection.
- **Founded:** 2023, London, UK. Founder: Chris Battarbee.
- **Funding:** ~$500K seed. Investors: Y Combinator (S23), Apertu Capital, XG Ventures.
- **OTel relationship:** Uses eBPF for zero-instrumentation data collection, exports to OTel-compatible formats. One Helm install with no code changes.
- **Key differentiation:** Extremely capital-efficient -- 3-person team generating $330K revenue (September 2025). Purpose-built for K8s only (not trying to be general-purpose). Guardian AI learns normal cluster patterns and detects anomalies without requiring alert configuration. Supports eBPF-powered profiling down to function level.
- **Why they matter:** The "do one thing well" approach to K8s observability. Priced at $20/node/month vs. Datadog's significantly higher per-host pricing. If K8s observability becomes its own product category (rather than a feature of general APM), Metoro is well-positioned.
- Sources: [YC](https://www.ycombinator.com/companies/metoro), [Metoro](https://metoro.io/)

---

### Observe Inc
- **What they do:** AI-powered observability platform built on a telemetry data lake, real-time knowledge graph, and agentic AI SRE. Positioned as a Datadog/Splunk replacement for enterprises.
- **Founded:** November 2017, San Jose, CA. Founded by Sutter Hill Ventures. CTO: Philipp Unterbrunner.
- **Funding:** $156M Series C (July 2025, led by Sutter Hill Ventures, with Madrona, Alumni Ventures, Snowflake Ventures, Capital One Ventures). Total funding ~$230M+.
- **OTel relationship:** OTel-compatible ingestion. Uses OpenTelemetry for collection. Platform is backend-focused (data lake + knowledge graph), not instrumentation-focused.
- **Key differentiation:** 180% net revenue retention. Tripled revenue and doubled enterprise customer base in a year. Three core components: O11y Data Lake, O11y Knowledge Graph, O11y AI SRE. Processes 150+ PB of telemetry data.
- **Why they matter:** ACQUIRED BY SNOWFLAKE for ~$1B (announced January 2026, closed Q1 2026). Snowflake's largest acquisition ever. Signals that data platform companies see observability as a natural extension. The acquisition validates the "observability on a data lake" architecture.
- Sources: [Snowflake](https://www.snowflake.com/en/news/press-releases/snowflake-announces-intent-to-acquire-observe-to-deliver-ai-powered-observability-at-enterprise-scale/), [TechCrunch](https://techcrunch.com/2026/01/08/snowflake-announces-its-intent-to-buy-observability-platform-observe/), [Observe](https://www.observeinc.com/blog/redefining-observability-for-ai-era-156m-series-c-funding)

---

### Axiom
- **What they do:** Event data platform for observability and AI engineering. Petabyte-scale ingest with serverless querying and schema-less ingestion. Log management and observability for high-scale engineering teams.
- **Founded:** 2017, London/San Francisco. Founders: Neil Jagdish Patel, Gordon Allott, Seif Lotfy.
- **Funding:** $41.4M total across 3 rounds (Series B February 2025). Investors: Crane Venture Partners, plus angels Nat Friedman (ex-GitHub CEO) and Adam Wiggins (Heroku co-founder).
- **OTel relationship:** OTLP-compatible ingestion. Positions as a backend for OTel data. Not OTel-native in architecture but fully compatible.
- **Key differentiation:** Petabyte-scale with high data compression. Schema-less ingestion (no need to define schemas upfront). Pricing based on ingest volume (GiB/month). 40,000+ organizations including Luma AI, Asana, Plex.
- **Why they matter:** The "Vercel for observability" positioning -- developer-friendly, schema-less, generous free tier. Nat Friedman and Adam Wiggins as angels signal dev-tools community credibility. Growing quietly while others fight over APM.
- Sources: [Axiom](https://axiom.co/), [Axiom blog](https://axiom.co/blog/axiom-raises-7m-to-cure-data-headaches), [TechCrunch](https://techcrunch.com/2020/06/09/data-startup-axiom-secures-4m-from-crane-venture-partners-emerges-from-stealth/)

---

### OpenObserve (O2)
- **What they do:** Open-source observability platform unifying logs, metrics, traces, frontend monitoring, and session replay. Written in Rust, built on Apache Parquet.
- **Founded:** 2022. Backed by Nexus Venture Partners, Dell Technologies Capital, Secure Octane.
- **Funding:** $3.6M seed (2022).
- **OTel relationship:** OTel-compatible ingestion. OTLP-native. Prices based on OTel-standard data.
- **Key differentiation:** Claims 140x lower storage costs vs. Elasticsearch via Apache Parquet columnar storage. Single-binary deployment. 2.6TB/day ingestion on a single node. 15,000+ GitHub stars. AGPL-3.0 licensed.
- **Why they matter:** The "dramatically cheaper" angle. If storage cost is the main pain point (and it is for many teams), OpenObserve's Rust + Parquet architecture is a compelling technical answer. The 140x storage cost reduction claim, if even partially accurate, changes the economics of self-hosted observability.
- Sources: [GitHub](https://github.com/openobserve/openobserve), [OpenObserve](https://openobserve.ai/), [OpenObserve blog](https://openobserve.ai/blog/openobserve-reaches-15000-github-stars/)

---

### Middleware
- **What they do:** AI-based full-stack cloud observability platform. Unified telemetry (logs, metrics, traces, RUM) with AI-driven insights and auto-instrumentation.
- **Founded:** 2021, San Francisco. YC W23.
- **Funding:** $6.5M seed (2023). Led by 8VC. Participants: Fin Capital, Guillermo Rauch (Vercel CEO), Tokyo Black, Decent Capital, Begin Capital, Beat Venture, Gokul Rajaram.
- **OTel relationship:** Built on OpenTelemetry. Auto-instrumentation via OTel Operator for Python, Node.js, Java, .NET, Golang. OTel Collector integration for data ingestion.
- **Key differentiation:** Per-core pricing model (unusual in the space). Real User Monitoring including Core Web Vitals and planned native iOS/Android support. Log pattern recognition that identifies similar logs across machines. Cloud + database integrations (AWS, GCP, MongoDB, Redis).
- **Why they matter:** The "Datadog feature set at startup pricing" play. Having Guillermo Rauch (Vercel) as an investor signals credibility with the frontend/fullstack developer community. The per-core pricing model could be disruptive if it resonates.
- Sources: [VentureBeat](https://venturebeat.com/ai/middleware-raises-6-5m-to-simplify-cloud-monitoring-with-ai), [YC](https://www.ycombinator.com/companies/middleware), [Middleware](https://middleware.io/)

---

### Last9
- **What they do:** Unified observability platform for logs, traces, metrics, and alerting. Flagship product Levitate is a time-series and events warehouse designed for high-cardinality environments.
- **Founded:** 2020, Sunnyvale, CA (India-based team). Founders: Nishant Modak, Piyush Verma, Kuldeep Dhankar.
- **Funding:** $13M total. Series A $11M (led by Sequoia Capital India / Peak XV Partners). Seed $2M (Surge, Better Capital). Angels from Hashicorp, GoJek, Razorpay, Sendbird, Scopely.
- **OTel relationship:** Fully OpenTelemetry compatible. Supports both gRPC and HTTP endpoints for OTel ingestion. Levitate integrates directly with OTel Collector.
- **Key differentiation:** 20M+ cardinality per metric -- purpose-built for K8s environments with dynamic labels and tags. Streaming aggregations for real-time data processing. Cardinality Explorer for visibility into metric behavior (vs. competitors that simply drop high-cardinality data). Pre-ingestion workflows to filter/enrich data before storage.
- **Why they matter:** High-cardinality metrics is a genuine unsolved problem that causes bill shock at Datadog. Last9 attacks the specific technical bottleneck (cardinality explosion in K8s) rather than trying to be a general-purpose platform. Sequoia India backing gives them credibility and a path into the large Indian engineering team market (Flipkart, Razorpay, etc.).
- Sources: [Last9](https://last9.io/), [Last9 Series A](https://last9.io/blog/announcing-our-series-a/), [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-56pbvyoa4ecja)

---

### Uptrace
- **What they do:** OpenTelemetry-native observability platform for distributed tracing, metrics, and logs. Built from the ground up around OTel specifications.
- **Founded:** ~2021-2022 (estimated). Founded by Vladimir Mihailenco (Moldova-based, also creator of popular Go libraries go-redis and bun).
- **Funding:** No disclosed external funding. Appears bootstrapped.
- **OTel relationship:** Fully OTel-native -- built entirely on OpenTelemetry with no proprietary agents. Uses ClickHouse as the storage backend. Supports Go, Node.js, Python, Java, .NET via OTel SDKs.
- **Key differentiation:** Self-hostable and cloud-hosted. Free tier with 1TB storage and 100K timeseries. The "small and simple" OTel backend. SQL querying. Very lightweight operational footprint.
- **Why they matter:** Represents the "OTel makes it possible for one person to build a viable observability backend" thesis. If OTel commoditizes collection, the backend becomes a commodity too -- and Uptrace shows how thin the backend layer can be.
- Sources: [Uptrace](https://uptrace.dev/), [GitHub](https://github.com/uptrace/uptrace)

---

### OneUptime
- **What they do:** Open-source observability platform combining monitoring, status pages, incident management, on-call scheduling, logs, and APM in a single solution.
- **Founded:** Unknown (pre-2023). MIT-licensed.
- **Funding:** No disclosed external funding.
- **OTel relationship:** OTel-compatible. Supports OTLP ingestion.
- **Key differentiation:** Breadth of feature set in a single open-source tool -- monitoring, APM, logs, traces, incidents, on-call, AND status pages. MIT license (most permissive). Claims 70-90% savings vs. Datadog + StatusPage + PagerDuty stack. Free self-hosted option.
- **Why they matter:** The "consolidation in a box" play. While most startups pick one slice (tracing, or metrics, or incidents), OneUptime bundles everything. For small teams that can't afford multiple SaaS tools, it's compelling. The open-source community has grown steadily.
- Sources: [OneUptime](https://oneuptime.com), [GitHub](https://github.com/OneUptime/oneuptime)

---

### Embrace
- **What they do:** Mobile-first observability platform. The only user-focused, mobile-first observability solution built on OpenTelemetry. Covers iOS and Android.
- **Founded:** ~2019, based in US.
- **Funding:** Backed by NEA, AV8 (Allianz), Greycroft, Y Combinator, Eniac. Angels from PagerDuty, MoPub, TestFlight, Sendbird, Scopely founders. Amount undisclosed but multi-round.
- **OTel relationship:** Deep OTel commitment -- iOS and Android SDKs rebuilt on OTel (announced April 2024). Contributed Kotlin OTel implementation upstream. CNCF member. Participates in multiple OTel SIGs. SDKs export to any OTLP-capable backend.
- **Key differentiation:** Only OTel-native mobile observability platform. Customers: NYT, Marriott, Warby Parker, Masterclass, Home Depot, Cameo. Mobile is a massive blind spot in traditional APM -- most tools focus on backend/server-side.
- **Why they matter:** Mobile observability is an underserved niche. As mobile apps become more complex (especially with on-device AI), the need for mobile-specific observability grows. Embrace's contribution of Kotlin OTel implementations back to the community gives them credibility and influence in OTel's mobile strategy.
- Sources: [Embrace](https://embrace.io/), [YC](https://www.ycombinator.com/companies/embrace), [Grafana blog](https://grafana.com/blog/2024/06/11/mobile-app-observability-with-opentelemetry-embrace-and-grafana-cloud/)

---

### Bindplane (observIQ)
- **What they do:** OTel-native telemetry pipeline management. Manages and configures OpenTelemetry Collectors at scale. Deepening Google Cloud partnership.
- **Founded:** ~2020. Based in US.
- **Funding:** Undisclosed. Google Cloud partnership is the key strategic relationship.
- **OTel relationship:** Core contributor to OpAMP (Open Agent Management Protocol) within OTel. Builds directly on the OTel Collector. The "Collector management layer."
- **Key differentiation:** Fills the gap between "we deployed OTel Collectors" and "we can actually manage thousands of Collectors in production." OpAMP contribution positions them at an important infrastructure layer.
- **Why they matter:** As OTel Collector deployments scale in enterprises, managing and configuring them becomes a real operational challenge. Bindplane is one of the few companies focused specifically on this layer. The Google partnership makes them the de facto Collector management tool for GCP users.
- Sources: [Bindplane](https://bindplane.com/), [Bindplane blog](https://bindplane.com/blog/from-kubecon-eu-to-kubecon-na-bindplane-s-opentelemetry-contributions-and-highlights-mar-oct-2025)

---

## Part 2: AI Observability and LLM Monitoring

### Langfuse (acquired by ClickHouse)
- **What they do:** Open-source LLM engineering platform -- tracing, evals, prompt management, monitoring for LLM applications.
- **Founded:** 2023. Founders: Marc Klingen, Max Deichmann, Clemens Rawert. YC W23.
- **Funding:** Backed by Y Combinator, Lightspeed Venture Partners, General Catalyst. ACQUIRED BY CLICKHOUSE (January 2026) as part of ClickHouse's $400M Series D at $15B valuation.
- **OTel relationship:** OTel-integrated tracing. Supports OpenTelemetry for collecting LLM trace data.
- **Key differentiation:** 2,000+ paying customers. 26M+ SDK installs/month. 6M+ Docker pulls. Used by 19 of the Fortune 50. Fastest-growing LLM observability tool before acquisition. Remains open source and self-hostable post-acquisition.
- **Why they matter:** The Langfuse acquisition is the template for how AI observability startups get acquired -- database company buys the observability layer to become the AI data platform. ClickHouse now owns both the storage engine and the AI observability UX. This pattern will repeat.
- Sources: [ClickHouse blog](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability), [SiliconANGLE](https://siliconangle.com/2026/01/16/database-maker-clickhouse-raises-400m-acquires-ai-observability-startup-langfuse/)

---

### Traceloop / OpenLLMetry (acquired by ServiceNow)
- **What they do:** LLM observability platform built on OpenLLMetry, an open-source extension of OpenTelemetry for LLMs. Provides tracing and quality checks (faithfulness, relevance) for LLM calls in production.
- **Founded:** ~2023, Israel. Founders: Nir Gazit (CEO, ex-Fiverr chief architect, ex-Google ML), Gal Kleinman (CTO).
- **Funding:** $6.1M seed (led by Sorenson Capital, Ibex Investors, with Samsung NEXT, Y Combinator, Grand Ventures). ACQUIRED BY SERVICENOW (March 2026) for estimated $60-80M.
- **OTel relationship:** THE bridge between OTel and LLMs. OpenLLMetry is a set of OTel extensions that provide observability for LLM applications using standard OTel protocols. Data can flow to any OTel-compatible backend (Datadog, Honeycomb, New Relic, etc.). OpenLLMetry remains open source post-acquisition.
- **Key differentiation:** OpenLLMetry is the de facto open-source standard for LLM tracing via OTel. ServiceNow acquiring them validates the "OTel for AI" thesis. Integration into ServiceNow's AI Control Tower.
- **Why they matter:** The $60-80M exit on $6.1M in funding is an excellent return. More importantly, OpenLLMetry becoming part of ServiceNow means enterprise adoption of OTel-based LLM observability will accelerate. The open-source commitment post-acquisition is notable.
- Sources: [Traceloop blog](https://traceloop.com/blog/traceloop-is-joining-servicenow), [Calcalist](https://www.calcalistech.com/ctechnews/article/sjghwiqf11e), [Sorenson Capital](https://www.sorensoncapital.com/from-traceloop-to-servicenow-how-ai-observability-became-the-missing-layer-in-enterprise-agent-systems/)

---

### Helicone (acquired by Mintlify)
- **What they do:** Open-source LLM observability platform and AI gateway. Unified view of performance, cost, and user interaction metrics for LLM providers (OpenAI, Anthropic, LangChain, etc.).
- **Founded:** ~2022. YC W23. Founders: Justin Torre, Cole Gottdank.
- **Funding:** $5M seed (October 2025, $25M valuation). Led by YC, Village Global, FundersClub. ACQUIRED BY MINTLIFY (March 3, 2026).
- **OTel relationship:** Compatible with OTel. Functions as both an AI gateway (routing, fallbacks) and an observability layer. Integrates with Vercel AI SDK.
- **Key differentiation:** Processed 2B+ LLM interactions. 16,000 organizations. Rust-based architecture (Cloudflare Workers, ClickHouse, Kafka). One-line integration. Functions as both proxy/gateway AND observability -- the "two products in one" angle.
- **Why they matter:** The Mintlify acquisition is an unusual pattern -- a documentation company buying an LLM observability company. It signals that AI observability is becoming a feature embedded in developer tools, not just a standalone product. Helicone services remain live in maintenance mode.
- Sources: [Helicone blog](https://www.helicone.ai/blog/joining-mintlify), [Mintlify blog](https://www.mintlify.com/blog/mintlify-acquires-helicone), [SalesTools](https://salestools.io/en/report/helicone-5m-seed)

---

### Highlight.io (acquired by LaunchDarkly)
- **What they do:** Open-source full-stack monitoring: error monitoring, session replay, logging, distributed tracing. Frontend-first observability.
- **Founded:** 2023, Seattle. Founders: Jay Khatri, Vadim Korolik. YC W23.
- **Funding:** $8M seed (led by Afore Capital and Craft Ventures, with YC, Neo, Day One Ventures, Worklife Ventures, Fuel Capital). ACQUIRED BY LAUNCHDARKLY (April 23, 2025).
- **OTel relationship:** Built on OTel framework. Supports both Highlight SDKs and direct OTel/OTLP ingestion. ClickHouse-powered backend.
- **Key differentiation:** Session replay synced with backend traces -- trace an error from button click to downstream log. 5,000+ GitHub stars pre-acquisition. Open-source (now integrated into LaunchDarkly's "Guarded Releases" product).
- **Why they matter:** The LaunchDarkly acquisition shows feature flagging companies moving into observability. The "deploy a feature flag, then immediately see its impact via observability" loop is a natural product extension. This is the "observability as a feature" pattern.
- Sources: [LaunchDarkly](https://launchdarkly.com/blog/welcome-highlight-to-launchdarkly/), [GlobeNewsWire](https://www.globenewswire.com/news-release/2025/04/23/3066295/0/en/LaunchDarkly-Acquires-Highlight-to-Advance-the-Future-of-Guarded-Software-Releases.html)

---

### Laminar
- **What they do:** Open-source observability platform purpose-built for AI agents. Traces complex multi-step agent workflows, replays and debugs agent runs, detects anomalies across trajectories.
- **Founded:** 2024, YC S24.
- **Funding:** $3M seed (March 2026). Led by Atlantic.vc. Participants: Y Combinator, AAL.vc. Notable angel: Ben Sigelman (OTel co-creator).
- **OTel relationship:** OpenTelemetry-native tracing SDK. Auto-traces Vercel AI SDK, Browser Use, Stagehand, LangChain, OpenAI, Anthropic, Gemini. OpenTelemetry is the protocol layer.
- **Key differentiation:** Purpose-built for AI agents that run for hours and generate thousands of spans (not just simple LLM calls). Browser agent support with synchronized video recording + traces ("flight recorder for AI"). Built in Rust for performance. Ingests 100s of GB daily. SQL access to all trace data.
- **Why they matter:** As AI agents become more autonomous and long-running, traditional LLM observability (designed for single API calls) breaks down. Laminar is betting on "agent debugging" as a distinct category. Ben Sigelman as an angel is a strong signal.
- Sources: [Tech.eu](https://tech.eu/2026/03/17/agent-debugging-startup-laminar-raises-3m-seed-to-tackle-the-observability-gap-in-ai-agents/), [Laminar](https://laminar.sh/), [GitHub](https://github.com/lmnr-ai/lmnr)

---

### Respan (formerly Keywords AI)
- **What they do:** Self-driving observability, evals, and gateway for AI agents. Proactive AI observability platform that doesn't just monitor but takes action to improve agent performance.
- **Founded:** YC-backed (batch unclear). Formerly known as Keywords AI.
- **Funding:** $5M (March 2026). From Gradient, Y Combinator, Hat-Trick Capital, XIAOXIAO FUND, Antigravity Capital, Alpen Capital, plus prominent AI founder angels.
- **OTel relationship:** Not OTel-native -- proprietary tracing and evaluation pipeline optimized for AI agent workflows.
- **Key differentiation:** First "proactive" AI observability -- automated evaluation agent that defines success with metric-first workflows, continuously evaluates production agent behavior, and turns results into actions (prompt updates, regression checks, alerts). 100+ AI startups + enterprise teams. 1B+ logs, 2T+ tokens/month, 6.5M+ end users.
- **Why they matter:** The shift from "observe and alert" to "observe and fix" is potentially the next evolution of AI observability. If AI agent quality can be automatically maintained (not just monitored), the TAM expands from DevOps to product teams.
- Sources: [GlobeNewsWire](https://www.globenewswire.com/news-release/2026/03/18/3258291/0/en/Respan-Announces-5M-in-Funding-from-Gradient-Y-Combinator-and-others-Launches-First-Proactive-AI-Observability-Platform.html), [YC](https://www.ycombinator.com/companies/respan)

---

### Confident AI / DeepEval
- **What they do:** LLM evaluation and observability platform. Powered by DeepEval, the most widely adopted open-source LLM evaluation framework (12K+ GitHub stars, 3M+ monthly downloads).
- **Founded:** 2024. Founders: Jeffrey Ip, Kritin Vongthongsri.
- **Funding:** $2.2M seed (August 2025, closed in 5 days). Investors: Y Combinator, Flex Capital, Oliver Jung, Vermilion Cliffs Ventures, Liquid 2 Ventures, January Capital, Rebel Fund.
- **OTel relationship:** Not OTel-native. Focus is on evaluation metrics rather than tracing/telemetry.
- **Key differentiation:** DeepEval is used by teams at OpenAI, Google, Microsoft. End-to-end LLM testing suite: benchmark LLM systems, compare prompts/models, catch regressions. 14+ evaluation metrics including hallucination detection, faithfulness, relevance. The "testing framework" angle rather than "monitoring" angle.
- **Why they matter:** If LLM evaluation becomes as standard as unit testing, Confident AI owns the open-source framework. The "raised $2.2M seed in 5 days" story indicates strong investor demand. DeepEval's adoption by OpenAI and Google is a powerful signal.
- Sources: [Confident AI blog](https://www.confident-ai.com/blog/how-i-closed-confident-ais-2-2m-seed-round-in-5-days), [GitHub](https://github.com/confident-ai/deepeval), [DeepEval](https://deepeval.com)

---

### Langtrace (Scale3 Labs)
- **What they do:** Open-source, OpenTelemetry-based end-to-end observability for LLM applications. Real-time tracing, evaluations, and metrics for LLMs, frameworks, vectorDBs.
- **Founded:** ~2022 (as Scale3 Labs).
- **Funding:** $5.3M seed (October 2022). Investors: Redpoint Ventures, Mysten Labs, plus one unnamed investor.
- **OTel relationship:** Built directly on OpenTelemetry. OTel-based tracing is the core architecture. Spans and traces follow OTel conventions.
- **Key differentiation:** OpenTelemetry-native LLM observability (vs. Langfuse which added OTel compatibility). Supports 30+ integrations: CrewAI, DSPy, LlamaIndex, Langchain. TypeScript and Python SDKs. NextJS frontend, PostgresDB metadata, ClickHouse for spans/metrics/traces. Self-hostable.
- **Why they matter:** One of the few LLM observability tools that is truly OTel-native (not just OTel-compatible). If OTel's GenAI semantic conventions become the standard, Langtrace is already aligned. The Redpoint backing gives credibility.
- Sources: [GitHub](https://github.com/Scale3-Labs/langtrace), [Langtrace](https://www.langtrace.ai/), [Tracxn](https://tracxn.com/d/companies/scale3-labs/__y3T6YUyQTSJC_vPhsY_scWn2xLLmBfhtrsWq41lhxug/funding-and-investors)

---

### OpenLIT
- **What they do:** Open-source, OpenTelemetry-native GenAI and LLM application observability platform. Vendor-neutral SDKs for Python, TypeScript, Go.
- **Founded:** February 2024. Non-profit / open-source project.
- **Funding:** No disclosed funding.
- **OTel relationship:** Deeply OTel-native. Built entirely on OTel framework. Sends traces and metrics to any OTel-compatible backend. One of the projects pushing OTel GenAI semantic conventions.
- **Key differentiation:** 50+ integrations (LLM providers, VectorDBs, agent frameworks, GPUs). 11 built-in evaluation types (hallucination, bias, toxicity, safety). GPU monitoring alongside LLM observability. Custom pricing files for cost tracking of fine-tuned models. One-line integration.
- **Why they matter:** The "OpenTelemetry Contrib for AI" play. Integrated with New Relic, Elastic, Grafana documentation as the recommended LLM observability layer. If OpenLIT becomes the standard OTel SDK extension for AI, every OTel backend automatically gains AI observability.
- Sources: [OpenLIT](https://openlit.io), [GitHub](https://github.com/openlit/openlit), [New Relic docs](https://docs.newrelic.com/docs/opentelemetry/get-started/openlit-llm-observability/openlit-llm-observability-intro/)

---

### Pydantic Logfire
- **What they do:** AI and application observability platform from the team behind Pydantic (the Python validation library used by virtually every AI/ML project). Production-grade observability for AI and general applications.
- **Founded:** Pydantic founded 2017 by Samuel Colvin; Logfire product launched 2024.
- **Funding:** Pydantic: $17.2M total. Series A $12.5M (October 2024, led by Sequoia Capital, with Partech, Irregular Expression). Seed $4.7M. Angels include Logan Kilpatrick (ex-OpenAI) and Jason Liu.
- **OTel relationship:** Built on OpenTelemetry. "Opinionated wrapper around OpenTelemetry." Native SDKs for Python, TypeScript, Rust. Leverages existing OTel instrumentation for common Python packages.
- **Key differentiation:** Pydantic is used by virtually every Python AI/ML project (FastAPI, LangChain, etc.). Built-in distribution advantage -- Logfire can be added to any Pydantic-using project with minimal friction. SQL querying of trace data. See LLM interactions, agent behavior, API requests, and DB queries in one unified trace.
- **Why they matter:** The "distribution moat" play. Pydantic has massive Python mindshare. If even a small percentage of Pydantic users adopt Logfire, it becomes one of the most widely-used observability tools for Python AI applications. Sequoia leading the Series A is a strong endorsement.
- Sources: [Logfire](https://pydantic.dev/logfire), [TechCrunch](https://techcrunch.com/2024/10/01/sequoia-backs-pydantic-to-expand-beyond-its-open-source-data-validation-framework/), [GitHub](https://github.com/pydantic/logfire)

---

### InfiniteWatch
- **What they do:** AI-native platform for agentic customer interaction intelligence. Monitors AI agents across voice and web channels. Session Replay Agent and Voice Agent products.
- **Founded:** October 2025, New York and Madrid. Founded by ex-CoverWallet leadership team (CoverWallet scaled to $1B+ premium revenue, acquired by Aon).
- **Funding:** $4M pre-seed (December 2025). Led by Base10 Partners. Participation: Sequoia and A16Z scouts, Kibo Ventures, Kfund, LifeX, four unicorn founders.
- **OTel relationship:** Not explicitly OTel-native. Focus is on customer interaction monitoring rather than infrastructure telemetry.
- **Key differentiation:** Targets "agentic customer interaction intelligence" -- monitoring AI agents that interact with customers (not developer tools or infrastructure). Analyzes 2M+ customer interactions/month. Session Replay + Voice Agent products. Enterprise customers in financial services, e-commerce, healthcare.
- **Why they matter:** A different take on AI observability -- focused on the customer-facing side rather than the developer/ops side. As companies deploy customer-facing AI agents (chatbots, voice agents), someone needs to monitor quality. InfiniteWatch is early to this specific niche.
- Sources: [PR Newswire](https://www.prnewswire.com/news-releases/infinitewatch-announces-4m-pre-seed-led-by-base10-partners-to-power-agentic-customer-interaction-intelligence-302646343.html), [TechFundingNews](https://techfundingnews.com/infinitewatch-4m-ai-agent-observability/)

---

### Lemma
- **What they do:** Evaluation and observability platform for AI agents with continuous learning -- not just measuring performance but automatically improving it.
- **Founded:** 2025 (YC F25 batch). Founders: Jerry and Cole, previously at Tandem (AI for healthcare) and Chipstack (AI for chip design).
- **Funding:** YC F25 standard deal (~$500K).
- **OTel relationship:** Not explicitly OTel-native. Focus is on evaluation and prompt optimization rather than telemetry infrastructure.
- **Key differentiation:** The "closed loop" approach -- agents learn from real user feedback and production data, then prompts automatically optimize. Claims teams cut manual prompt iteration by 90%, resolve production drifts in minutes, improve model performance 2-5% per optimization cycle. Live drift detection and regression alerts.
- **Why they matter:** If the thesis is correct that AI observability evolves from "watch and alert" to "watch and automatically improve," Lemma is the earliest embodiment. Very early stage but the YC F25 stamp and the specific founding team background (healthcare AI + chip design AI) suggests they've experienced the problem firsthand.
- Sources: [Lemma](https://www.uselemma.ai/), [YC](https://www.ycombinator.com/companies/uselemma), [Fondo](https://www.fondo.com/blog/lemmaf25-launches)

---

### Baserun
- **What they do:** Testing and observability platform for LLM applications. Helps AI teams test, evaluate, and monitor LLM features.
- **Founded:** 2023, San Francisco. Founders: Adam Ginzberg, Effy Zhang (CEO).
- **Funding:** $500K (YC only). YC is the sole institutional investor.
- **OTel relationship:** Not explicitly OTel-native.
- **Key differentiation:** Streamlines the development cycle from identifying an issue to evaluating the solution. Testing-first approach to LLM observability.
- **Why they matter:** Very early stage. Minimal funding. Worth watching if they can differentiate on the "testing" angle, but faces stiff competition from Confident AI/DeepEval, Langfuse, and others.
- Sources: [YC](https://www.ycombinator.com/companies/baserun)

---

### Ember Robotics
- **What they do:** Hardware and system observability for robots and IoT devices. Edge-first diagnostics platform. "Datadog for robots."
- **Founded:** 2024, San Francisco. Founders: Shivani Mouleeswaran (ex-Tesla Autopilot, 5+ years on camera systems for autonomous vehicles), Ritika Shrivastava (ex-Tesla Autopilot, computer vision).
- **Funding:** YC-backed (batch unclear). Early stage.
- **OTel relationship:** Not OTel-focused. Hardware/edge observability is a different domain from cloud-native telemetry.
- **Key differentiation:** Camera diagnostics for robots. Edge-first (not cloud-first). Targets the gap between "we built a robot" and "we can monitor a fleet of robots in production." Tesla Autopilot pedigree.
- **Why they matter:** A niche play, but if robotics scales (warehouse robots, delivery robots, autonomous vehicles), someone needs to do fleet-wide observability for physical systems. Traditional APM tools don't work for hardware. Very early but unique positioning.
- Sources: [YC](https://www.ycombinator.com/companies/ember-robotics), [Ember](https://www.emberrobotics.com/)

---

### Ryvn
- **What they do:** Infrastructure for deploying SaaS in customer clouds (BYOC) with built-in observability. Targets sensitive industries (healthcare, finance, manufacturing).
- **Founded:** 2025 (estimated), New York. YC-backed. Team from Palantir, Vercel, Capital One.
- **Funding:** YC seed stage.
- **OTel relationship:** Observability is a feature of the deployment platform, not the core product. Likely OTel-compatible for the observability component.
- **Key differentiation:** BYOC (Bring Your Own Cloud) deployment with observability baked in. Solves the "enterprise security review" problem for SaaS companies selling to regulated industries. The observability is the value-add that makes BYOC deployments manageable.
- **Why they matter:** Tangential to pure observability, but the "observability as a feature of BYOC deployment" pattern could become important as more enterprises demand data residency and on-prem deployment of SaaS tools.
- Sources: [YC](https://www.ycombinator.com/companies/ryvn), [Ryvn](https://ryvn.ai/)

---

## Part 3: Acquisitions Summary (2025-2026)

| Company | Acquirer | Date | Est. Value | Prior Funding |
|---------|----------|------|-----------|---------------|
| Observe Inc | Snowflake | Jan 2026 | ~$1B | ~$230M+ |
| Langfuse | ClickHouse | Jan 2026 | Undisclosed | YC + Lightspeed + GC |
| Traceloop | ServiceNow | Mar 2026 | $60-80M | $6.1M |
| Helicone | Mintlify | Mar 2026 | Undisclosed | $5M |
| Highlight.io | LaunchDarkly | Apr 2025 | Undisclosed | $8M |
| Aporia | Coralogix | Jan 2025 | Undisclosed | N/A |
| Lumigo | Dash0 | Feb 2026 | Undisclosed | N/A |

**Pattern:** Acquirers are database companies (ClickHouse, Snowflake), platform companies (ServiceNow), developer tool companies (LaunchDarkly, Mintlify), and observability consolidators (Dash0, Coralogix). AI observability startups are being acquired at 10-13x their funding amount (Traceloop: $6.1M raised, $60-80M exit).

---

## Part 4: Key Patterns Across the Long Tail

1. **OTel-native is mandatory.** Every funded startup in 2024-2026 is either built on OTel or fully OTel-compatible. No proprietary-only instrumentation company has received funding.

2. **eBPF + OTel convergence.** Odigos, Coroot, Metoro, and Groundcover all use eBPF for zero-code instrumentation. The OTel eBPF Instrumentation SIG is standardizing this approach. eBPF eliminates the instrumentation barrier that slowed OTel adoption.

3. **AI observability is fragmenting into sub-categories:**
   - LLM call tracing (Langfuse, Traceloop/OpenLLMetry, Langtrace, OpenLIT)
   - AI agent debugging (Laminar, Respan)
   - LLM evaluation/testing (Confident AI/DeepEval, Baserun)
   - Customer-facing AI monitoring (InfiniteWatch)
   - Continuous AI improvement (Lemma, Respan)

4. **ClickHouse is the default storage engine.** Langfuse, Highlight.io, Helicone, SigNoz, Laminar, OpenObserve, Langtrace, and others all use ClickHouse. ClickHouse acquiring Langfuse signals they want to own the AI observability layer on top of their storage.

5. **Rapid acqui-hire cycle.** Multiple startups (Helicone, Highlight.io, Traceloop) were acquired within 2-3 years of founding. The AI observability space moves too fast for big companies to build internally, so they buy.

6. **"Observability as a feature" trend.** LaunchDarkly (feature flags), Mintlify (docs), Snowflake (data platform), ClickHouse (database) are all adding observability as a feature of their core platform rather than building standalone observability products.

7. **Bootstrapped alternatives are viable.** Coroot, Uptrace, OneUptime, and OpenLIT show that OTel's commoditization of collection makes it possible to build viable observability tools without VC funding.
