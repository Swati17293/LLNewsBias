from eventregistry import *
import csv 
import time


csvfile = open('election.csv', 'a', newline='\n')
writer = csv.writer(csvfile, delimiter=',')

er = EventRegistry(apiKey = 'add-your-own-key')

# conceptUri = QueryItems.OR([er.getConceptUri("coronavirus"),er.getConceptUri("covid"),er.getConceptUri("covid19")]),
# conceptUri = er.getConceptUri("ukrainian crisis"),


# en cz      hr      ro          pl      si          fi          se      es      fr      it      dk      ua      nl          be      at      de
# czech   croatia romania     poland  slovenia    finland     sweden  spain   france  italy   denmark ukraine netherlands belgium austria germany

label_list = ['LC','LB','LB','LC','LC','LC','LB','LC','LC','RC','RC','RC','LC','RC','RC','LC','LC','LC','LC','RC','LC','LC','LB','LB','RC','RC','LC','LC','LC','RC','RC','LB','RC','LB','LB','RC','LB','LC','RC','LC','LC','RC','LC','LB','RC']
src_list = ['index.hr','agerpres.ro','digi24.ro','novinky.cz','hotnews.ro','wyborcza.pl','24ur.com','delo.si','hs.fi','gp.se','expressen.se','dn.se','elpais.com','abc.es','elmundo.es','eldiario.es','publico.es','francetvinfo.fr','mediapart.fr','lefigaro.fr','repubblica.it','finanza.lastampa.it','ansa.it','corriere.it','berlingske.dk','bt.dk','pravda.com.ua','censor.net','nos.nl','volkskrant.nl','ad.nl','bnr.nl','lalibre.be','lesoir.be','hln.be','standaard.be','derstandard.at','diepresse.com','ladepeche.fr','liberation.fr','welt.de','spiegel.de','zdf.de','faz.net']


# concept_list_war = ['https://en.wikipedia.org/wiki/Casualties_of_the_Russo-Ukrainian_War',
# 'http://en.wikipedia.org/wiki/Ukrainian_crisis',
# 'http://en.wikipedia.org/wiki/Little_green_men_(Ukrainian_crisis)',
# 'http://en.wikipedia.org/wiki/Media_portrayal_of_the_Ukrainian_crisis'
# 'http://en.wikipedia.org/wiki/List_of_people_sanctioned_during_the_Ukrainian_crisis',
# 'http://en.wikipedia.org/wiki/International_sanctions_during_the_Ukrainian_crisis',
# 'https://en.wikipedia.org/wiki/Russia–Ukraine_gas_disputes',
# 'https://en.wikipedia.org/wiki/Russia%E2%80%93Ukraine_gas_disputes',
# 'https://en.wikipedia.org/wiki/Nuclear_threats_during_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/Reactions_to_the_2021–2022_Russo-Ukrainian_crisis',
# 'https://en.wikipedia.org/wiki/Reactions_to_the_2021%E2%80%932022_Russo-Ukrainian_crisis',
# 'https://en.wikipedia.org/wiki/Corporate_responses_to_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/Reactions_to_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/War_crimes_in_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/Russian_people\'s_militias_in_Ukraine',
# 'https://en.wikipedia.org/wiki/Russian_people%27s_militias_in_Ukraine']

# concept_list_war = ['https://en.wikipedia.org/wiki/List_of_foreign_aid_to_Ukraine_during_the_Russo-Ukrainian_War',
# 'https://en.wikipedia.org/wiki/International_sanctions_during_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/Humanitarian_impact_of_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/Allegations_of_genocide_of_Ukrainians_in_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/Agreement_on_settlement_of_political_crisis_in_Ukraine',
# 'https://en.wikipedia.org/wiki/Russo-Ukrainian_War',
# 'https://en.wikipedia.org/wiki/Ukraine_Crisis_Media_Center',
# 'https://en.wikipedia.org/wiki/Prelude_to_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/Economic_impact_of_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/2022_Ukrainian_refugee_crisis',
# 'https://en.wikipedia.org/wiki/International_sanctions_during_the_Russo-Ukrainian_War',
# 'https://en.wikipedia.org/wiki/Disinformation_in_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/Media_portrayal_of_the_Russo-Ukrainian_War',
# 'https://en.wikipedia.org/wiki/Russo-Ukrainian_War',
# 'https://en.wikipedia.org/wiki/Prelude_to_the_2022_Russian_invasion_of_Ukraine',
# 'https://en.wikipedia.org/wiki/Ukrainian–Soviet_War',
# 'https://en.wikipedia.org/wiki/Ukrainian%E2%80%93Soviet_War',
# 'https://en.wikipedia.org/wiki/Russo-Ukrainian_War']
# czech   croatia romania     poland  slovenia    finland     sweden  spain   france  italy   denmark ukraine netherlands belgium austria germany

# concept_list = ['https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Albania',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Austria',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Belarus',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Belgium',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Bulgaria',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Croatia',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Czech_Republic',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Denmark',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Estonia',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Finland',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_France',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Germany',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Hungary',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Iceland',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Ireland',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Italy',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Latvia',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Norway',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Poland',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Portugal',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Romania',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Russia',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Serbia']


# concept_list = ['https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Slovakia',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Slovenia',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Spain',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Sweden',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Switzerland',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Ukraine',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_Kingdom ',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Vatican_City',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_Netherlands',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Europe',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Asia',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Africa']



# concept_list = ['https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_2019',
# 'https://en.wikipedia.org/wiki/COVID-19_rapid_antigen_test',
# 'https://en.wikipedia.org/wiki/Economic_impact_of_the_COVID-19_pandemic',
# 'https://en.wikipedia.org/wiki/History_of_COVID-19_vaccine_development',
# 'https://en.wikipedia.org/wiki/COVID-19_lab_leak_theory',
# 'https://en.wikipedia.org/wiki/COVID-19_testing',
# 'https://en.wikipedia.org/wiki/2022_COVID-19_protests_in_China',
# 'https://en.wikipedia.org/wiki/Investigations_into_the_origin_of_COVID-19',
# 'https://en.wikipedia.org/wiki/COVID-19_lockdowns',
# 'https://en.wikipedia.org/wiki/Pfizer%E2%80%93BioNTech_COVID-19_vaccine',
# 'https://en.wikipedia.org/wiki/COVID-19_misinformation',
# 'https://en.wikipedia.org/wiki/Symptoms_of_COVID-19',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Russia',
# 'https://en.wikipedia.org/wiki/List_of_deaths_due_to_COVID-19',
# 'https://en.wikipedia.org/wiki/Oxford%E2%80%93AstraZeneca_COVID-19_vaccine',
# 'https://en.wikipedia.org/wiki/Chinese_government_response_to_COVID-19',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory',
# 'https://en.wikipedia.org/wiki/List_of_COVID-19_vaccine_authorizations',
# 'https://en.wikipedia.org/wiki/Long_COVID',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_South_Africa',
# 'https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_education',
# 'https://en.wikipedia.org/wiki/COVID-19_lockdowns_by_country',
# 'https://en.wikipedia.org/wiki/Janssen_COVID-19_vaccine',
# 'https://en.wikipedia.org/wiki/Moderna_COVID-19_vaccine',
# 'https://en.wikipedia.org/wiki/COVID-19_lab_leak_theory',
# 'https://en.wikipedia.org/wiki/COVID-19_vaccine',
# 'https://en.wikipedia.org/wiki/COVID-19']


# concept_list = ['https://en.wikipedia.org/wiki/COVID-19_pandemic_deaths',
# 'https://en.wikipedia.org/wiki/Treatment_and_management_of_COVID-19',
# 'https://en.wikipedia.org/wiki/COVID-19_deaths',
# 'https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_the_environment',
# 'https://en.wikipedia.org/wiki/List_of_unproven_methods_against_COVID-19',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_New_York_City',
# 'https://en.wikipedia.org/wiki/Transmission_of_COVID-19',
# 'https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic',
# 'https://en.wikipedia.org/wiki/COVID-19_misinformation_by_China',
# 'https://en.wikipedia.org/wiki/COVID-19_drug_development',
# 'https://en.wikipedia.org/wiki/COVID-19_protests_in_Germany',
# 'https://en.wikipedia.org/wiki/COVID-19_apps',
# 'https://en.wikipedia.org/wiki/COVID-19_vaccination_in_India',
# 'https://en.wikipedia.org/wiki/COVID-19_vaccine_clinical_research',
# 'https://en.wikipedia.org/wiki/COVID-19_party',
# 'https://en.wikipedia.org/wiki/COVID-19_lockdown_in_China',
# 'https://en.wikipedia.org/wiki/Sputnik_V_COVID-19_vaccine',
# 'https://en.wikipedia.org/wiki/U.S._federal_government_response_to_the_COVID-19_pandemic',
# 'https://en.wikipedia.org/wiki/COVID-19_vaccine_card',
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_on_cruise_ships',
# 'https://en.wikipedia.org/wiki/Novel_coronavirus',  
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic',
# 'https://en.wikipedia.org/wiki/Coronavirus',
# 'https://en.wikipedia.org/wiki/Novel_coronavirus',
# 'https://en.wikipedia.org/wiki/SARS-CoV-2']


# concept_list = ['https://en.wikipedia.org/wiki/Brexit',
# 'https://en.wikipedia.org/wiki/Brexit_withdrawal_agreement',
# 'https://en.wikipedia.org/wiki/Brexit_and_the_Irish_border',
# 'https://en.wikipedia.org/wiki/Brexit_negotiations_in_2018',
# 'https://en.wikipedia.org/wiki/Brexit_negotiations_in_2019',
# 'https://en.wikipedia.org/wiki/Brexit_negotiations_in_2020',
# 'https://en.wikipedia.org/wiki/Brexit_negotiations_in_2021',
# 'https://en.wikipedia.org/wiki/Brexit_negotiations_in_2017',
# 'https://en.wikipedia.org/wiki/Brexit_Party_election_results',
# 'https://en.wikipedia.org/wiki/Brexit_in_popular_culture',
# 'https://en.wikipedia.org/wiki/Brexit:_The_Uncivil_War',
# 'https://en.wikipedia.org/wiki/Brexit_and_arrangements_for_science_and_technology',
# 'https://en.wikipedia.org/wiki/Brexit_negotiations',
# 'https://en.wikipedia.org/wiki/Border_Communities_Against_Brexit',
# 'https://en.wikipedia.org/wiki/Post-Brexit_United_Kingdom_relations_with_the_European_Union',
# 'https://en.wikipedia.org/wiki/Brexitcast',
# 'https://en.wikipedia.org/wiki/Trade_negotiation_between_the_UK_and_the_EU',
# 'https://en.wikipedia.org/wiki/Department_for_Exiting_the_European_Union',
# 'https://en.wikipedia.org/wiki/International_reactions_to_the_2016_United_Kingdom_European_Union_membership_referendum',
# 'https://en.wikipedia.org/wiki/Campaigning_in_the_2016_United_Kingdom_European_Union_membership_referendum',
# 'https://en.wikipedia.org/wiki/Get_Brexit_Done',
# 'https://en.wikipedia.org/wiki/European_Union_(Withdrawal)_Act_2018']


# concept_list = ['https://en.wikipedia.org/wiki/Opinion_polling_for_the_United_Kingdom_European_Union_membership_referendum',
# 'https://en.wikipedia.org/wiki/EU%E2%80%93UK_Trade_and_Cooperation_Agreement',
# 'https://en.wikipedia.org/wiki/Brexit_divorce_bill',
# 'https://en.wikipedia.org/wiki/Secretary_of_State_for_Exiting_the_European_Union',
# 'https://en.wikipedia.org/wiki/Get_ready_for_Brexit',
# 'https://en.wikipedia.org/wiki/Bollocks_to_Brexit',
# 'https://en.wikipedia.org/wiki/Endorsements_in_the_2016_United_Kingdom_European_Union_membership_referendum',
# 'https://en.wikipedia.org/wiki/Brexit_Party_election_results',
# 'https://en.wikipedia.org/wiki/Brexit_plan',
# 'https://en.wikipedia.org/wiki/Aftermath_of_the_2016_United_Kingdom_European_Union_membership_referendum',
# 'https://en.wikipedia.org/wiki/BrexitCentral',
# 'https://en.wikipedia.org/wiki/Predicted_impact_of_Brexit',
# 'https://en.wikipedia.org/wiki/Brexit_opinion_polls',
# 'https://en.wikipedia.org/wiki/Impact_of_Brexit_on_the_European_Union',
# 'https://en.wikipedia.org/wiki/Russian_interference_in_the_2016_Brexit_referendum',
# 'https://en.wikipedia.org/wiki/Proposed_referendum_on_the_Brexit_withdrawal_agreement',
# 'https://en.wikipedia.org/wiki/Parliamentary_votes_on_Brexit',
# 'https://en.wikipedia.org/wiki/Brexit_Alliance',
# 'https://en.wikipedia.org/wiki/Brexit_and_the_Irish_border',
# 'https://en.wikipedia.org/wiki/Brexit_negotiations',
# 'https://en.wikipedia.org/wiki/Brexit_vote',
# 'https://en.wikipedia.org/wiki/Brexit:_The_Uncivil_War',
# 'https://en.wikipedia.org/wiki/No-deal_Brexit',
# 'https://en.wikipedia.org/wiki/Opposition_to_Brexit',
# 'https://en.wikipedia.org/wiki/Timeline_of_Brexit',
# 'https://en.wikipedia.org/wiki/Economic_effects_of_Brexit',
# 'https://en.wikipedia.org/wiki/2016_United_Kingdom_European_Union_membership_referendum',
# 'https://en.wikipedia.org/wiki/Causes_of_the_vote_in_favour_of_Brexit',
# 'https://en.wikipedia.org/wiki/Reform_UK',
# 'https://en.wikipedia.org/wiki/Brexit']


concept_list = ['https://en.wikipedia.org/wiki/United_States_presidential_elections_in_Arkansas',
'https://en.wikipedia.org/wiki/United_States_presidential_elections_in_the_District_of_Columbia',
'https://en.wikipedia.org/wiki/United_States_presidential_elections_in_Arizona',
'https://en.wikipedia.org/wiki/United_States_presidential_elections_in_Utah',
'https://en.wikipedia.org/wiki/United_States_presidential_elections_in_California',
'https://en.wikipedia.org/wiki/United_States_presidential_elections_in_New_Mexico',
'https://en.wikipedia.org/wiki/United_States_presidential_elections_in_Pennsylvania',
'https://en.wikipedia.org/wiki/United_States_presidential_elections_in_Ohio',
'https://en.wikipedia.org/wiki/United_States_presidential_elections_in_Alaska',
'https://en.wikipedia.org/wiki/2012_United_States_presidential_election',
'https://en.wikipedia.org/wiki/United_States_presidential_election',
'https://en.wikipedia.org/wiki/2008_United_States_presidential_election',
'https://en.wikipedia.org/wiki/2020_United_States_presidential_election',
'https://en.wikipedia.org/wiki/2024_United_States_presidential_election',
'https://en.wikipedia.org/wiki/United_States_presidential_election']





# 'https://en.wikipedia.org/wiki/R_(Miller)_v_Secretary_of_State_for_Exiting_the_European_Union'



# concept_list = ['http://en.wikipedia.org/wiki/Coronavirus','http://es.wikipedia.org/wiki/Pandemia_de_COVID-19','http://en.wikipedia.org/wiki/COVID-19','http://en.wikipedia.org/wiki/Long_COVID']

# concept_list = ['http://en.wikipedia.org/wiki/Ukraine_Crisis_Media_Center','http://en.wikipedia.org/wiki/Ukrainian_crisis']

# concept_list = ['http://en.wikipedia.org/wiki/2020_United_States_presidential_election','http://en.wikipedia.org/wiki/United_States_presidential_election,_2020','http://en.wikipedia.org/wiki/Attempts_to_overturn_the_2020_United_States_presidential_electiohtn','http://en.wikipedia.org/wiki/2020_United_States_presidential_election_in_Kentucky','http://en.wikipedia.org/wiki/2020_United_States_presidential_election_in_Georgia']


# concept_list = ['http://it.wikipedia.org/wiki/UEFA_Nations_League_2020-2021'] (only 21)

# concept_list = ['http://en.wikipedia.org/wiki/2019_Amazon_rainforest_wildfires'] (none)


# q = QueryArticlesIter(
#     conceptUri = er.getConceptUri("ukrainian crisis"),
#     sourceUri = QueryItems.OR(src_list))

q = QueryArticlesIter(
    conceptUri = QueryItems.OR(concept_list),
    sourceUri = QueryItems.OR(src_list))


cnt = 0
for article in q.execQuery(er, sortBy = "rel", 
        returnInfo = ReturnInfo(articleInfo = ArticleInfoFlags(body = False, url = False, eventUri = False, authors = False, concepts = False, categories = True, dates = False, image =False)),
        maxItems = -1):

    row_text = []
    row_text.append(article['source']['uri'])

    try:
        bias_index = src_list.index(article['source']['uri'])
        row_text.append(label_list[bias_index])
    except:
        row_text.append('unidentified')
    
    row_text.append(article['uri'])
    row_text.append(article['lang'])
    row_text.append(article['date'])
    row_text.append(article['title'])
    for i in range(0,len(article['categories'])):
        row_text.append(article['categories'][i]['uri'])
        break


    if len(article['categories']) > 0:
        writer.writerow(row_text)

    cnt += 1
    print(cnt)

    time.sleep(0.05)




    
    
    