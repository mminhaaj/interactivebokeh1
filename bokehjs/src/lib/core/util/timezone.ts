const tz = require("timezone")

export default function(value: unknown, format?: string): string {
    return tz(value, format)
}
