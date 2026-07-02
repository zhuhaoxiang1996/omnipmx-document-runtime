# xskills Operator Notes

These notes summarize the platform manual requirements relevant to this package.

## Upload Contract

Prepare a local Skill folder containing:

- `SKILL.md`
- role files such as `agents/*.md`
- reference files such as `references/*.md`
- optional examples or validation files

Compress the entire folder. The platform recommends `.zip` and also supports `.tar.gz`, `.tar`, `.rar`, and `.7z`.

Upload through Skill Management -> Upload Skill. After upload, the skill appears under My Skills. Enable it before using it in chat.

## Editing And Validation

Use Skill Edit to inspect or modify files. After every edit, click "Save Markdown"; otherwise changes will not take effect.

In chat, use:

- `/` to manually select a Skill.
- `#` to select uploaded reference files.
- the model switcher to choose DeepSeek or another model.

Validate with at least 5 fixed cases whose expected conclusions are known. In detailed mode, check:

1. whether the correct Skill was triggered;
2. whether the expected agent/reference files were read;
3. whether the reasoning chain follows the intended workflow;
4. whether the finalization gate prevents premature final claims.

## Recommended First Test

Prompt:

```text
/OmniPMX toolkit-v0.1
我要做 ADC 类药物 payload 的 PBPK。请以 MMAE 为 payload，先不要声称执行检索；请生成 PubMed 检索交接包、导出 manifest 模板、筛选标准和最终报告前置门控。
```

Expected behavior:

- The model should generate search strings and manifest requirements.
- It should leave counts as `待数据库回填`.
- It should not claim a final report is complete.
- It should include a finalization gate with `INTERIM_NOT_FINAL` or `BLOCKED_WAITING_FOR_INPUT`.
