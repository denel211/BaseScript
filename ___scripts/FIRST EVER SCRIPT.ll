var naam = input "Hoe heet je? >> ";
var leeftijd = input "Hoe oud ben je? >> ";
var stad = input "In welke stad woon je? >> ";

var meerdereJaren = (leeftijd isnt "1");
var nietMeerdereJaren = (leeftijd is "1");

if meerdereJaren: log "U heet " .. naam .. ", u bent " .. leeftijd .. " jaren oud en u woont in " .. stad .. ".";
if nietMeerdereJaren: log "U heet " .. naam .. ", u bent " .. leeftijd .. " jaar oud en u woont in " .. stad .. ".";