
SELECT
	handlers.name AS handler_name,
	owners.name AS owner_name,
	dogs.name AS dog_name,
	appointments.request,
	appointments.time
FROM owners
JOIN dogs
	ON owners.id = dogs.owner_id
JOIN appointments
	ON appointments.dog_id = dogs.id
JOIN handlers
	ON appointments.handler_id = handlers.id
ORDER BY appointments.time DESC LIMIT 1;


SELECT
	handlers.name,
	COUNT(appointments.id) AS appt_count
FROM handlers
JOIN appointments
	ON appointments.handler_id = handlers.id
GROUP BY handler_id
HAVING appt_count > 1;