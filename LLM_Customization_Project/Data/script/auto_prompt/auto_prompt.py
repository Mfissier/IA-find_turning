import itertools
import random

# Define possible categories with their specific relationships
categories = {
    "Name": ["Name"],
    "Action": ["Name", "Object", "Location", "Event"],
    "Object": ["Object"],
    "Location": ["Location"],
    "Emotion": ["Name"],
    "Relationship": ["Name"],
    "Status": ["Name"],
    "Characteristic": ["Name", "Object"],
    "Event": ["Location", "Name"],
    "Organization": ["Name", "Action", "Object"]
}

def requires_link(cat1, cat2):
    if cat1 == "Name":
        return cat2 in ["Action", "Emotion", "Relationship", "Characteristic", "Status"]
    elif cat1 == "Action":
        return cat2 in ["Object", "Location", "Event"]
    elif cat1 == "Object":
        return cat2 in ["Location", "Event", "Characteristic"]
    elif cat1 == "Location":
        return cat2 in ["Organization", "Event", "Characteristic"]
    elif cat1 == "Organization":
        return cat2 in ["Event", "Relationship", "Characteristic", "Status"]
    elif cat1 == "Event":
        return cat2 == "Characteristic"
    elif cat1 == "Emotion":
        return cat2 == "Relationship"
    elif cat1 == "Relationship":
        return cat2 in ["Characteristic", "Status"]
    return False

def generate_prompt_examples():
    max_phrases = 10
    max_occurrences = 5
    results = []
    count = 0

    for r in range(1, len(categories) + 1):
        # Generate all possible combinations of categories of length r
        category_combinations = list(itertools.combinations(categories.keys(), r))

        # For each combination of categories
        for combination in category_combinations:
            num_phrases = random.randint(1, max_phrases)

            for phrase_count in range(1, num_phrases + 1):
                count += 1
                example_phrases = []
                expected_output = []
                category_id_map = {cat: idx + 1 for idx, cat in enumerate(combination)}

                for cat in combination:
                    num_occurrences = random.randint(1, max_occurrences)
                    for occurrence in range(1, num_occurrences + 1):
                        cat_id = category_id_map[cat]
                        linked_cat = None

                        for other_cat in combination:
                            if other_cat != cat and requires_link(cat, other_cat):
                                linked_cat = other_cat
                                linked_cat_id = category_id_map[linked_cat]
                                break
                        # Construct the phrase and expected format
                        if linked_cat:
                            phrase_example = f"{cat} ({linked_cat}: example_{occurrence})"
                            expected_format = f"{cat} : example_{occurrence} [{cat_id}] [{linked_cat_id}]"
                        else:
                            phrase_example = f"{cat} (ex: example_{occurrence})"
                            expected_format = f"{cat} : example_{occurrence} [{cat_id}]"

                        example_phrases.append(phrase_example)
                        expected_output.append(expected_format)

                sentence = " ".join(example_phrases)
                output = ", ".join(expected_output)

                prompt_description = f"""
Explanation for data labeling:
You will receive sentences containing different categories. Your task is to analyze each sentence and label the elements according to the defined categories and subcategories. Here are the instructions:
Main categories: Each element in a sentence corresponds to a specific category (e.g., Name, Action, Object, Location, Emotion, etc.).
Links and associations: Some elements in a sentence are linked to each other by their category:
A Name can be associated with an Action, Emotion, Relationship, or Location.
An Object can be associated with a Location or an Action.
Links are indicated by ID numbers in brackets [ ] for each category. These IDs help to understand the associations (e.g., Name : Alice [1] and Action : runs [1] indicate that Alice runs).
Expected output example:
Sentence: Alice runs in the park with a ball.
Labeling:
Name : Alice [1]
Action : runs [1][3]
Location : park [1]
Object : ball [1][4]
Expected output: Name : Alice [1], Action : runs [1][3], Location : park [1], Object : ball [1][4]
Number of phrases: The examples can contain 1 to 10 sentences with a varied set of categories and associations in each sentence.
Labeling a response: Provide a structured list of each category followed by the relevant element and its identifier.
Please generate according to this prompt (you can adjust the links as needed for coherence):
Prompt with {phrase_count} sentence(s) containing the categories: {', '.join(combination)}.
Sentence: {sentence}
Expected output: {output}
                """

                # Add to results list
                results.append(prompt_description)

                # Print for verification
                print(prompt_description)
                print("-" * 40)
    print("Total number of prompts generated:", count)
    return results

generate_prompt_examples()
