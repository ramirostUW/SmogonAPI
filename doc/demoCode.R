library("rjson")


getAvgAttackStat <- function(json_url){
   json_data <- fromJSON(paste(readLines(json_url), collapse=""))
   attack_stat_vector <- c()
   for(pokemon in json_data){
     attack_stat_vector <- c(attack_stat_vector, pokemon[["atk"]])
   }
   return(sum(attack_stat_vector)/length(attack_stat_vector))
}

list_of_gens <- c(
  "rb",
  "gs",
  "rs",
  "dp", 
  "bw",
  "xy",
  "sm",
  "ss",
  "sv"
)
api_endpoint_url <- "https://smogonapi.herokuapp.com/GetPokemonByGen/"
attackStats <- data.frame(gen = list_of_gens, 
                          url = (paste0(api_endpoint_url, list_of_gens, "/")))
attackStats$atk <- -1

for(index in 1:length(attackStats$url)){
  url <- attackStats$url[index]
  attackStats[index, "atk"] <- getAvgAttackStat(url)
}

barplot(attackStats$atk, names.arg = attackStats$gen, xlab ="Gen", 
        ylab ="Avg. Atk", col ="green", 
        main ="Average Atk across Gens")
