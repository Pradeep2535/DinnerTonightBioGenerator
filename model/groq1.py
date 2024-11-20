import json
from groq import Groq

class LlamaModel:
    def __init__(self):
        self.model = Groq(api_key="GROQ_API_KEY")
    def generate_response(self, career, personality, interests, relationship_goals):

        completion = self.model.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            
            {
                "role": "user",
                "content": " \"User Input Career: Entrepreneur\\nPersonality: Energetic\\nInterests: Fitness, Outdoor Adventures\\nRelationship Goals: Long-term\",\n        \"Output The Sporty Entrepreneur\\n\\nEnergetic entrepreneur with a passion for fitness and outdoor adventures. Seeking a partner who can keep up with my active lifestyle and shares my love for hiking, biking, and trying new things.\",\n        \"User Input Career: Musician\\nPersonality: Compassionate\\nInterests: Live Music, Social Justice\\nRelationship Goals: Casual\",\n        \"Output The Compassionate Musician\\n\\nSoulful musician with a heart for social justice and a love for live music. Looking for a kind and compassionate partner who enjoys jamming out at concerts and making a difference in the world.\",\n        \"User Input Career: Software Engineer\\nPersonality: Tech-Savvy\\nInterests: Gaming, Technology\\nRelationship Goals: Casual\",\n        \"Output The Tech-Savvy Gamer\\n\\nSoftware engineer by day, gamer by night. I'm equally comfortable debugging code and exploring virtual worlds. Seeking a partner who can appreciate my geeky side and isn't afraid to challenge me to a board game showdown.\",\n        \"User Input Career: "+str(career) + "\nPersonality: " + str(personality) + "\nInterests: " + str(interests) + "\nRelationship Goals: " + str(relationship_goals)+"\",\n        \"Output \",\n        \"give the output, like the same format topic,description as given in examples.And take reference from examples and give output for the last input passed and it should include both topic and description. it should also be capitilized properly.Give in JSON format - topic and description.Each time give unique responses.\"\n"
            },
            
            
        ],
        temperature=1,
        max_tokens=7930,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
        )
        try:
            formatted_response = json.loads(completion.choices[0].message.content)

            output_topic = formatted_response["topic"]
            output_description = formatted_response["description"]
        except:
            output_topic = "Please Try Again"
            output_description = ""

        #print(output_topic,output_description)

        return output_topic, output_description



