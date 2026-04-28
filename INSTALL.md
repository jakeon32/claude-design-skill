# Claude Design — 설치 가이드

이 플러그인은 SKILL 1개 + sub-agent 13개로 구성됩니다. Claude Code 안에서 슬래시 명령으로 설치합니다.

---

## 빠른 설치 (3-step)

### 1) 구조 검증 (옵션 — 권장)

repo 루트에서:

```powershell
# Windows (PowerShell)
.\install.ps1
```

```bash
# Mac / Linux
./install.sh
```

스크립트는 파일 구조만 검증하고 슬래시 명령을 클립보드에 복사합니다 (Claude Code 자체는 외부에서 자동화 불가).

### 2) Claude Code에서 슬래시 명령 실행 — **한 줄씩 따로**

> ⚠️ **3줄을 한꺼번에 paste하지 말 것.** `/plugin marketplace add` 는 인자를 받지 않고 인터랙티브 prompt(`Enter marketplace source:`)를 띄우는 형태라, 한 번에 paste하면 뒤의 두 줄이 그 prompt의 입력으로 흡수되어 `Path does not exist` 에러가 납니다.

**Step 1**: 명령만 입력 → Enter
```
/plugin marketplace add
```
→ "Enter marketplace source:" prompt가 뜨면 거기에 repo 절대경로만 paste:
```
D:\claude\claude-skills\claude-design-v3
```
→ Enter

**Step 2**: 새 줄에 입력 → Enter
```
/plugin install claude-design@claude-design-local
```

**Step 3**: 새 줄에 입력 → Enter
```
/reload-plugins
```

> 경로는 자신의 repo 루트 절대경로로 교체. install 스크립트가 이미 클립보드에 path만 복사해 둡니다 (Step 1의 prompt 입력용).

### 3) 설치 확인

```
/plugin
```

→ **Installed** 탭에 `claude-design` 표시 확인.

---

## 동작 검증

설치 직후 다음을 확인:

| 검사 | 명령 | 기대 결과 |
|-----|-----|---------|
| Skill 활성화 | `/claude-design` | "Claude Design" 스킬 진입 |
| Agent 등록 | 자연어 "디자인 만들어줘" | `Agent` tool이 `claude-design:project-planner` 호출 가능 |
| 트리거 단어 | "발표 슬라이드", "프로토타입" 등 | SKILL 자동 진입 |

Agent tool에서 직접 호출하려면 `subagent_type` 에 namespace 포함:
- `claude-design:project-planner`
- `claude-design:design-system-manager`
- `claude-design:slide-deck-agent` (메인 generator — 2회 호출 패턴)
- `claude-design:slide-qa-agent` (자동 후속 호출)
- `claude-design:slide-pptx-agent` (선택 — "PPTX로" 요청 시)
- `claude-design:prototype-agent` / `document-agent` / `other-agent`
- `claude-design:visual-refiner`
- 옵션 4종: `copywriting-agent` / `animation-agent` / `responsive-agent` / `accessibility-agent`

---

## 트러블슈팅

### "Agent type 'claude-design:project-planner' not found"
- `/plugin` 에서 `claude-design` 이 Installed 탭에 있는지 확인
- 안 보이면 `/plugin install claude-design@claude-design-local` 다시 실행
- 변경 후 `/reload-plugins` 안 했을 가능성

### `/plugin marketplace add` 가 디렉토리를 못 찾음 — `Path does not exist:` 에러
- **가장 흔한 원인**: 슬래시 명령 3줄을 한 번에 paste한 경우. `/plugin marketplace add` 는 prompt 모드라 paste의 다음 줄들이 source 인자로 흡수됨. **Esc로 취소 후 한 줄씩 다시 입력**.
- 경로는 절대경로 권장 (Windows: `D:\...`, Mac/Linux: `/Users/...`)
- 경로에 한글·공백 있으면 따옴표로 감싸기: `"D:\내 경로\claude-design-v3"`
- repo 루트 안에 `.claude-plugin/marketplace.json` 있는지 확인

### `Marketplace configuration file is corrupted: <name>.source.source: Invalid input`
- **원인**: marketplace.json의 `plugins[].source` 가 단순 string인 경우. 객체 형식이어야 함.
- 우리 marketplace.json은 이미 올바른 형식이지만 fork/수정 시 주의:
  ```json
  "source": { "source": "directory", "path": "./plugins/claude-design" }
  ```
- 캐시된 corrupt entry가 남아있는 경우: `~/.claude/plugins/known_marketplaces.json` 백업 후 해당 marketplace entry 제거, `~/.claude/plugins/installed_plugins.json` 의 stale plugin entry도 같이 제거, 다시 `/plugin marketplace add` 시도

### Skill은 작동하는데 agent 호출이 실패
- agent .md 파일이 `plugins/claude-design/agents/` 에 있는지 확인 (skills 폴더 안 아님)
- `plugins/claude-design/.claude-plugin/plugin.json` 존재 확인
- `/reload-plugins` 실행

### PPTX 변환 도구가 작동 안 함
- `pip install -r plugins/claude-design/skills/claude-design/tools/requirements.txt`
- `playwright install chromium`
- Windows: PowerPoint 설치 필요 (PPTX → PNG)
- Pretendard 폰트 시스템 설치 권장 (`C:\Windows\Fonts\`)

---

## 업데이트

플러그인 코드를 수정한 뒤 (예: agent.md 추가/수정):

```
/reload-plugins
```

이걸로 즉시 반영. 새 agent를 등록하려면 plugin install이 다시 필요할 수 있음 — 안 잡히면:

```
/plugin uninstall claude-design@claude-design-local
/plugin install claude-design@claude-design-local
/reload-plugins
```

---

## 다른 머신으로 옮길 때

1. repo 전체를 복사 (또는 `git clone`)
2. 새 머신의 절대경로로 `/plugin marketplace add` 다시 실행
3. `/plugin install claude-design@claude-design-local`
4. `/reload-plugins`

`marketplace.json` 의 `source: "./plugins/claude-design"` 는 상대경로라 어떤 위치에서도 작동.

---

## 디렉토리 구조 참고

```
claude-design-v3/                     ← repo 루트 (=marketplace 추가 대상)
├── .claude-plugin/
│   └── marketplace.json              ← name: "claude-design-local"
├── plugins/claude-design/            ← 플러그인 루트
│   ├── .claude-plugin/
│   │   └── plugin.json               ← name/version/description
│   ├── agents/                       ← 자동 등록 위치 (13 .md)
│   └── skills/claude-design/
│       ├── SKILL.md
│       ├── references/               ← 디자인 레퍼런스 (스타일/레이아웃)
│       └── tools/                    ← Python 유틸 (PPTX)
├── install.ps1                       ← Windows 검증 스크립트
├── install.sh                        ← Mac/Linux 검증 스크립트
├── INSTALL.md                        ← 본 문서
└── CLAUDE.md                         ← 프로젝트 instructions
```
