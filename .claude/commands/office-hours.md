# Office Hours Skill

Use this skill to manage and communicate office hours availability for code reviews, pair programming, and technical discussions.

## When to Use

Invoke `/office-hours` when you want to:
- Check or display current office hours schedule
- Set availability windows for collaboration
- Communicate when you're available for async questions
- Schedule or plan office hours sessions

## Behavior

When invoked, this skill will:

1. **Check current schedule** - Look for any existing office hours configuration in the project
2. **Display availability** - Show when office hours are scheduled
3. **Update schedule** - Allow setting new office hours windows
4. **Generate summary** - Produce a clear, shareable availability block

## Output Format

Produce a formatted office hours block like:

```
## Office Hours

📅 Schedule: [Days and times]
🕐 Timezone: [Timezone]
📍 Location: [Virtual/Room/Link]
📝 Topics: [What you're available for]

To book time: [Instructions]
```

## Example Usage

When the user runs `/office-hours`, ask:
- What days/times are they available?
- What timezone?
- What topics or types of help will they offer?
- How should people reach out or book time?

Then generate the formatted output and optionally save it to a `OFFICE_HOURS.md` file or add it to an existing README.
