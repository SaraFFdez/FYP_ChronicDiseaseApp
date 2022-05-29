import AudioProcessing.symptoms_entity_ruler as symp
#from AudioProcessing.symptoms_entity_ruler import symptoms_identifier
import AudioProcessing.activity_entity_ruler as act
import AudioProcessing.food_diary_processing as food
# from AudioProcessing.activity_entity_ruler import activity_identifier
# from AudioProcessing.food_diary_processing import food_timing_identificator

#Input: a file/text containing the audio in the file
#Output: Lists/dictionaries containing the information we need
def speech_processing_main(input_text):
    symptomsList = symp.symptoms_identifier(input_text)
    foodDiary1 = food.food_timing_identificator(input_text)
    foodDiary2 = food.food_timing_identificator_modif(input_text)
    activityList = act.activity_identifier(input_text)

    return symptomsList, foodDiary1, foodDiary2, activityList