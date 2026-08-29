# Audit

Every important finding must answer:

- What evidence caused this constraint / warning / block?
- What changed since the previous verification?
- What branch state was used?
- What Arena material influenced this decision?

Answer by **reference** (branch, path, hash, class), not by copying source bodies into the skill.

The verification report (`schemas/verification-report.schema.json`) is the audit record. Post-generation reports bind the same `canon_state_id` and `contract_id`. Historical PASSes remain historical; they are not patched in place.
