# Banco de pruebas del ejecutor de acciones

Este PR existe para probar `AGENT-EXECUTOR-GITHUB` (RD-2753) contra una rama
protegida. `main` de este repo exige 1 aprobación, así que un `merge_pr` sin
aprobar debe devolver `blocked_by_branch_protection` y NO mergear.

El repo es **público** a propósito: branch protection no existe en repos
privados de plan free. No poner nada sensible acá.

Si alguien mergea este PR, abrir otro: el banco necesita un PR abierto.
