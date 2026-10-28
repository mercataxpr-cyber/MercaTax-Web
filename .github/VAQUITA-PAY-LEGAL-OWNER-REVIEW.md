# Vaquita Pay — revisión interna de decisiones legales

Documento interno de preparación. No está enlazado desde las seis páginas ni incluido en el sitemap. Resume decisiones aprobadas por el Owner y verificaciones que todavía impiden aprobar o publicar los borradores. No constituye asesoría ni certificación legal.

## Estado

Las seis páginas locales incorporan las decisiones operativas aprobadas y siguen siendo borradores sin fecha de vigencia. La aprobación del Owner cubre estas políticas, no la verificación legal o técnica ni la publicación. No se cambió el producto, infraestructura, configuración de retención, proveedores o documentos corporativos de MercaTax.

## Decisiones aprobadas e integradas

- **Operador:** MercaTax es el nombre comercial/DBA de un propietario individual registrado en Puerto Rico; no es LLC ni corporación independiente. No se inventó ni añadió el nombre legal completo del propietario.
- **Elegibilidad y contacto:** edad mínima de 18 años para Participantes y Organizadores. Contacto oficial para soporte, privacidad, eliminación y asuntos legales: mercataxpr@gmail.com; no se inventó un plazo de respuesta.
- **Jurisdicción:** Puerto Rico y legislación federal estadounidense aplicable, respetando derechos obligatorios de consumidores.
- **Reembolsos:** el Organizador evalúa y gestiona reembolsos ordinarios; MercaTax ofrece soporte técnico y herramientas. Se conservan excepciones para duplicados, errores de procesamiento, contracargos, fraude, obligaciones legales y derechos del consumidor. No hay garantía universal.
- **Whop:** el Organizador puede cancelar; cuando Whop hace efectiva la cancelación, conserva beneficios hasta terminar el período pagado y no hay renovaciones posteriores. La cancelación ordinaria no produce reembolso automático. Historial operativo: 12 meses desde terminación. Los cambios de plan no prorratean el período previo y los días no usados pueden no conservarse. Compras nativas siguen sin aprobación.
- **Moderación:** el Organizador modera contenido de sus campañas; MercaTax puede investigar reportes, retirar contenido y suspender por infracciones graves. Expedientes: 24 meses desde resolución, salvo excepción documentada. La política no afirma que Vaquita Pay tenga comentarios; se cubren si la función se habilita.
- **Eliminación:** objetivo máximo de 30 días desde solicitud validada y verificación de identidad; confirmar al usuario al completarse, sujeto a retenciones legales justificadas. Eliminar/anonimizar perfil y contenido personal innecesario; conservar registros financieros por separado cuando corresponda. No bloquear indefinidamente por una membresía.
- **Organizador:** cierre temporal separado de eliminación definitiva. Documentos de verificación, si se recopilan, pueden mantenerse hasta 90 días tras cierre temporal con necesidad justificada; retorno requiere autorización y aprobación, sin reactivación automática. Eliminación definitiva no espera 90 días; los documentos se suprimen salvo obligación específica.
- **Retención operativa:** comprobantes fiscales propios de MercaTax hasta 7 años sujeto a validar alcance, inicio y excepciones; no extender ese plazo a todas las aportaciones. Documentos de cuentas activas solo durante necesidad justificada; campañas operativas 12 meses desde cierre definitivo; membresía Whop 12 meses desde terminación; logs de seguridad 90 días; moderación y decisiones administrativas 24 meses desde resolución; respaldos ordinarios hasta 90 días sujetos a auditoría; caso mínimo de eliminación 24 meses desde cierre. Excepciones requieren motivo y fecha de revisión. El plazo técnico documentado de evidencia manual de un año queda pendiente de validación legal y operativa.
- **Campaña y descarga:** datos operativos 12 meses desde cierre definitivo; recibos accesibles solo cuando estén autorizados y disponibles, sin promesa de acceso indefinido. Descarga ZIP completa aprobada como requisito futuro, no implementada. Un recordatorio por campaña 30 días antes, por push/in-app y email, también es futuro; no extiende retención.
- **Ayuda de retención aprobada para futura integración móvil:** “El plazo empieza cuando la campaña se cierra definitivamente. Los datos operativos estarán disponibles durante 12 meses y podrás descargar la información permitida hasta la fecha exacta de vencimiento que se muestra aquí. Después, eliminaremos o anonimizaremos los datos operativos que ya no sean necesarios. Los registros financieros que debamos conservar por ley se mantienen por separado.”

## Evidencia técnica estática revisada en Vacana (solo lectura)

- La app tiene ruta de eliminación dentro de Perfil con reautenticación y un proceso backend; esta revisión no ejecutó una solicitud ni confirmó purga de todos los proveedores/datos ni la notificación final.
- La página pública de eliminación en MercaTax sigue siendo informativa: no presenta formulario ni tramita automáticamente. El inicio por Centro Legal debe implementarse y validarse. El comportamiento actual frente a renovaciones/operaciones abiertas debe conciliarse con el máximo de 30 días.
- Existen opciones de reportar noticias y bloquear Organizadores en la app, y una superficie de revisión Owner; no se verificó el servicio operativo/SLA. No se encontró una función de comentarios habilitada. Las funciones de retirar contenido/suspender cuentas requieren validación operativa antes de describirlas como disponibles.
- La documentación de producto registra cancelación de membresías reemplazadas como una obligación pendiente hasta una observación de Whop que confirme que no renueva o terminó; la llamada de cancelación de Whop no está implementada. La política aprobada no significa que haya un control de cancelación dentro de la app.
- No se confirmó recopilación/archivo actual de documentos de verificación de Organizadores, exportación ZIP, indicador de fecha de vencimiento, recordatorio 30 días antes, automatización de borrado/anonimización ni ejecución técnica de los plazos de backup.
- Esta revisión fue estática y de solo lectura. No se generaron datos de prueba, no se iniciaron flujos de pagos, no se consultaron servicios externos ni se modificó Vacana.

## Validaciones legales, contractuales y técnicas pendientes

1. Confirmar si y dónde debe aparecer el nombre legal completo del propietario del DBA y su dirección.
2. Determinar el alcance tributario de cobros propios de MercaTax frente a aportaciones de Organizadores.
3. Validar el inicio del cómputo, aplicación y excepciones de los siete años para comprobantes fiscales propios de MercaTax.
4. Confirmar si determinados documentos fiscales deben conservarse físicamente en Puerto Rico.
5. Determinar la clasificación regulatoria del flujo de fondos, si corresponde.
6. Auditar el flujo real de eliminación: solicitud desde app y web, validación de identidad, plazo máximo, datos relacionados, Storage, servicios externos, operaciones pendientes, retenciones justificadas y confirmación final.
7. Verificar qué documentos de Organizador se recopilan, necesidad, acceso, almacenamiento seguro, registro de cambios y eliminación temporal/definitiva.
8. Auditar respaldos reales, retención, restauración sin recuperar información personal eliminada y costo; no modificar TTL ni infraestructura en esta tarea.
9. Implementar y validar la solicitud web pública, exportación ZIP, fecha exacta de vencimiento y un recordatorio único 30 días antes.
10. Confirmar operación, responsables, control de acceso y respuesta de soporte/moderación; revisar categorías, reportes y suspensión/retirada.
11. Confirmar contratos y operación de Firebase, Stripe, PayPal y Whop, incluida cancelación efectiva y obligaciones de membresías sustituidas.
12. Completar App Privacy, Google Data Safety, declaraciones financieras, edad/contenido, reviewer access y materiales de tienda usando el inventario real de lanzamiento.
13. Validar el alcance y fundamento del plazo técnico de un año para evidencia de aportaciones manuales.
14. Revisar la redacción final con asesoría legal y obtener aprobación final del Owner antes de dar fecha de vigencia o publicar.

## Alcance de esta actualización

Modificados únicamente los seis documentos Vaquita Pay y este archivo interno. Sin cambios a terms.html, privacy.html, legal.css, sitemap.xml, Vacana, UpPaidPR, proveedores, DNS o sistemas de retención. Sin publicación, despliegue ni operaciones externas.