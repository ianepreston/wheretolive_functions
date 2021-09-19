# Triggering on debug
Under the timer trigger binding in function.json, add ```"runOnStartup": true,```
Should look something like this

```json
  "bindings": [
    {
      "runOnStartup": true,
      "type": "timerTrigger",
      "direction": "in",
      "name": "timer",
      "schedule": "0 0 6 * * *"
    },
```