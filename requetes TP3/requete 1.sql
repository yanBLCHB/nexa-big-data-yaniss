SELECT
`Station en fonctionnement`,
COUNT(*) AS nb_stations
FROM `global-brook-483613-r9.dataset_velib.velib`
GROUP BY `Station en fonctionnement`;