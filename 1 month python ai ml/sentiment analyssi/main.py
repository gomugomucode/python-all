"""
Twitter Sentiment Analysis Pipeline
==================================
This script cleans a list of raw tweets, extracts sentiment polarity and subjectivity 
using TextBlob, categorizes sentiment (Positive, Negative, Neutral), displays analysis metrics, 
and exports the processed dataset to a CSV file.
"""

import os
import re
import string
import pandas as pd
from textblob import TextBlob

# ----------------------------------------------------
# 1. Raw Tweet Data
# ----------------------------------------------------
final_my_tweet = [
    "Tweets",
    "@balen_shah1 Good 😊😊",
    "@belakoboli khasai kei gareko ta xainan balen dai le yeti bidi jholey tarika le raja sanga comapre nagareko vaye hu… https://t.co/UOBy38KitJ",
    "The master of corruption of my country: The President, Prime Minister, Minister, MP, MLA, Mayor and even the Ward C… https://t.co/tOaO6Vydvu",
    "@belakoboli One of the extremely rare occasions where I happen to agree with this guy, even if partially. Although… https://t.co/zq3ORYvsvy",
    "Balen during weekends! 🤔\n\n https://t.co/OS44uOMGjE",
    "Balen and Sampang effect in federal elections https://t.co/6lC0qdePoG via @TheAnnaExpress",
    "@machiel1 @albertheijn Whut? Balen!",
    "@BaldipChauhan @RabindraMishra Rabindra Mishra will never win. He ended his political career the moment he decided… https://t.co/9RucvbpnUm",
    "@balen_shah1 Proud of you @ShahBalen",
    "balen’s wife… i wasn’t familiar with his game",
    "@sanghiyawtie Balen is leading the metropolis while serving. k bhaneko mijyu yesto?😩",
    "@balen_shah1 Really nice pict thank you  keep going sir please I from Boston please 🙏",
    "RT @RoyalFamily: His Majesty The King gives a\xa0personal\xa0declaration at today’s Accession Council, where he was formally proclaimed King Char…",
    "@balen_shah1 Beautiful",
    "@kandeldai Jealousy against Balen",
    "RT @sanzinme: Hait #Balen 🔥🔥 https://t.co/QWjkBRUnFT",
    "Songs of LANY 🎵 🎶",
    'ELECTION 2022\n\n"Rise of independent candidates like Balen and Sampang at the local level has paved the path for sev… https://t.co/mmJVv2q645',
    "@balen_shah1 Fake Acount",
    "@balen_shah1 Good 🙏🙏",
    "@balen_shah1 Thank.",
    "RT @ShellenbergerMD: That's not the end of the story, of course. Farmers can fight back. We can show solidarity with them. \n\nIn Sri Lanka t…",
    "So nicely expressed ! Balen and the team should heed on the author's feedback. \n\n@kathmandupost, hilarious is the m… https://t.co/gwW3hknZHY",
    "@balen_shah1 Hero of nation",
    "@rameshore Balen is able to deliver, because he is professional and free to take his own decisions, unfettered by c… https://t.co/VDWM4kjDO0",
    "@balen_shah1 rell time rell king i love ..my heart contact fell",
    "@juction4love Before Balen, the President and the Prime Minister showed zero and\nthinking👇 🤔 👌😋 \nSame photo 👇👇terro… https://t.co/3b3CCb8x3V",
    "Balen is no less than a great celebrity!\n#BalenSupporter ✌️",
    "RT @RaameshKoirala: Is Balen a DON?\nNO.\nHe deserves extra 'e'.\nWell DONE!\n🙏🙏🙏🙏🙏",
    "When you're hangry af at a momo pasal and the server is down so you can't even watch balen's dozer on tiktok https://t.co/2ripYTt0mO",
    "I wonder will rabindra misra accept balen as new king when monarchy gets back?🤔",
    "RT @SarcasmNpl: Nothing interesting, just Routiney pretending Balen to be the king. https://t.co/0urZ0GuvGX",
    "@balen_shah1 Is Balen compairing himself with the king.... OMG ,",
    "but is Balen a leader at all? Isn’t he a public servant? https://t.co/USTKazCR0T",
    "@balen_shah1 Great Job",
    "RT @RONBupdates: Kathmandu Metro Mayor Balen Shah gave his presence during Indra Jatra at Basantapur yesterday and huge crowd of people was…",
    "RT Emily Ratajkowski slays Ratajkowski wearing Knwls Halcyon Long-Sleeved Top, Knwls Halcyon Flared Leggings, Balen… https://t.co/MRSzQQp7iF",
    "@NirmalPrasai5 Nirmal jee, I still remember you arguing with me on Twitter during the Mayoral election, saying Bale… https://t.co/oEq8stvZfp",
    "RT @arundadhikary: अब अरु लाई ridicule गरेर भोट जितिदैन ! Those days are gone ! You must stand out on your own merit without belittling you…",
    "RT @LawaRashid: Summer dump https://t.co/doppzTbq0t",
    "versace bottega praga balen vuitton dior givenchy",
    "bALEN'S Craze is evidence of hunger for good leadership in Nepal",
    "@balen_shah1 Nice pic",
    "The Balen brothers blew through the competition winning the first annual 2A District Doubles Invite tournament! Con… https://t.co/jwrp7ffmct",
    "@Split_72 How do you make SO MANY LEVELS",
    "@ShashankGhimir8 @balen_shah1 It’s fan page 😁",
    "RT @NoNext_Question: The video shows people’s craze and support for Kathmandu Metropolis Mayor Balen Shah during Indra Jatra festival held…",
    "@balen_shah1 Great effort. Well-done Balen, salute you 🌹",
    "@balen_shah1 Really proud of you and shine like our king  birendra. Always think about our nepali people and I am h… https://t.co/eJSsC2caiQ",
    "@balen_shah1 Keep up the good work ☺️",
    "Balen turning into a revolution. https://t.co/ygiKnuzHfe",
    "@parajulippradip @balen_shah1 This is the pic of the decade ❣️",
    "RT @SamratSpeaks: Balen is making us dormant folks realize what a leader should be, something we never had so far. Never in my life had I s…",
    "@balen_shah1 Great work",
    "It’s not a purse. It’s a Balen.",
    "@Dipendra02468 @balen_shah1 So it has been warned",
    "@Anjita_pandey Thnak you. I willbe there. Balen ko sahar ma ni aainus.. https://t.co/zZx4DQXzJW",
    "RT @_bishab: Balen turning into a revolution. https://t.co/ygiKnuzHfe",
    "@ShahBalen 200-300 paid actor everyday follows balen tetro berojgar ni chaina hola ni free ma nara lagayera balen b… https://t.co/yfVtLqPdKe",
    "@dipeshrisal This is another extreme ..sure Balen realizes it. Also King B did not have Balen kind of personality -… https://t.co/U6rjUeEiso",
    "@balen_shah1 Great job 👏",
    "@bahunnaran Balen is not king 👑💯👑 ok ...",
    "@theomeereboer Shit. Balen",
    "@creo_music I will gladly play the triple a price of 60 United States dollars for a Creo game",
    "RT @drs1k: @juction4love Before Balen, the President and the Prime Minister showed zero and\nthinking👇 🤔 👌😋 \nSame photo 👇👇terrorist https://…",
    "@iRiskant_ @NS_online Blegh, da's balen. 💔",
    "@balen_shah1 nice pic ....go ahead balen ji",
]


# ----------------------------------------------------
# 2. Text Normalization Function
# ----------------------------------------------------
def normalize_tweet(text: str) -> str:
    """
    Cleans raw tweet text by:
    - Removing HTML special entities (e.g. &amp;)
    - Removing Twitter user handles (@user)
    - Removing stock cashtags ($USD)
    - Converting text to lowercase
    - Removing HTTP/HTTPS links
    - Removing hashtag symbols (#)
    - Removing punctuation
    - Removing short words (1-2 characters)
    - Stripping extra whitespaces
    - Filtering non-standard Unicode characters
    """
    text = re.sub(r"\&\w*;", "", text)                            # Remove HTML entities
    text = re.sub(r"@[^\s]+", "", text)                           # Remove @mentions
    text = re.sub(r"\$\w*", "", text)                             # Remove cashtags ($)
    text = text.lower()                                           # Convert to lowercase
    text = re.sub(r"https?:\/\/.*\/\w*", "", text)               # Remove URLs
    text = re.sub(r"#\w*", "", text)                              # Remove hashtags
    text = re.sub(r"[" + string.punctuation.replace("@", "") + "]+", " ", text) # Remove punctuation
    text = re.sub(r"\b\w{1,2}\b", "", text)                       # Remove short words (1-2 chars)
    text = re.sub(r"\s\s+", " ", text)                            # Remove extra spaces
    text = re.sub(r"[^a-zA-Z]", " ", text)                        # Keep alphabetic letters only
    text = text.strip()                                           # Strip leading/trailing space
    text = "".join(c for c in text if c <= "\uffff")              # Clean unicode
    return text


# ----------------------------------------------------
# 3. Main Analysis Flow
# ----------------------------------------------------
def main():
    print("--- 1. Cleaning Raw Tweets ---")
    # Apply text normalization to all tweets
    cleaned_tweets = [normalize_tweet(tweet) for tweet in final_my_tweet]

    # Create Pandas DataFrame
    df = pd.DataFrame({"tweets": cleaned_tweets})

    # Filter out empty tweets resulting from cleaning
    df = df[df["tweets"].str.len() > 0]

    # Deduplicate tweets to remove retweets and duplicate entries
    df = df.drop_duplicates(subset="tweets").reset_index(drop=True)
    print(f"Total unique cleaned tweets ready for analysis: {len(df)}")

    # --- 2. Sentiment Analysis with TextBlob ---
    print("\n--- 2. Analyzing Sentiment (Polarity & Subjectivity) ---")
    # Apply TextBlob sentiment scoring
    df[["Polarity", "Subjectivity"]] = df["tweets"].apply(
        lambda text: pd.Series(TextBlob(text).sentiment)
    )

    # --- 3. Categorize Sentiment ---
    def categorize_polarity(polarity: float) -> str:
        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"

    df["sentiment"] = df["Polarity"].apply(categorize_polarity)

    # --- 4. Summarize Analysis Results ---
    print("\n--- 3. Sentiment Analysis Summary ---")
    sentiment_counts = df["sentiment"].value_counts()
    
    positive_count = sentiment_counts.get("Positive", 0)
    negative_count = sentiment_counts.get("Negative", 0)
    neutral_count = sentiment_counts.get("Neutral", 0)
    total_analyzed = len(df)

    print(f"Number of Tweets Analysed = {total_analyzed}")
    print(f"Positive tweets           = {positive_count}")
    print(f"Negative tweets           = {negative_count}")
    print(f"Neutral tweets            = {neutral_count}")

    # Display preview of results dataframe
    print("\n--- Sample Analyzed Data ---")
    print(df[["tweets", "Polarity", "Subjectivity", "sentiment"]].head(10))

    # --- 5. Export Processed Data ---
    output_file = "filtered_data.csv"
    df.to_csv(output_file, index=False)
    print(f"\nFiltered dataset saved successfully to: '{output_file}'")


if __name__ == "__main__":
    main()
