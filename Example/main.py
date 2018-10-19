from pywordcloud import WordCloudGenrator

test_txt = """The time has come. Electric scooter sharing services are returning to the streets
            of San Francisco — this time with explicit permission from the SF Municipal Transportation
            Agency. On Monday, we’ll see both Skip and Scoot deploy their respective electric scooters
            throughout the city.
            And if you remember what it was like earlier this year, you’ll likely notice that these
            scooters look different from the ones that were previously scattered throughout the city.
            In March, a number of electric scooters from Bird, Lime  and Spin appeared in San Francisco
            essentially overnight. That prompted city officials to act quickly, with the SF City 
            Attorney’s office sending cease-and-desist letters, a new city law going into in June 
            restricting electric scooter companies from operating without a permit and, eventually,
            the SFMTA creating a permitting process.
            But the permitting process and the decision that resulted did not sit well with companies
            like Lime and Lyft, which were not granted permits to operate electric scooter services in
            San Francisco. Toward the end of this week, Lime made clear its intentions to seek to block
            the deployment of scooters on Monday. A judge, however, denied Lime’s request for the temporary
            restraining order. Lyft had also petitioned SF Mayor London Breed, asking her to take a look at
            the SFMTA’s decision. Despite Lyft and Lime’s efforts, the great electric scooter rollout of 2018
            is still happening on Monday.
            Ahead of the official launch, TechCrunch chatted with Scoot CEO Michael Keating and Skip CEO Sanjay
            Dastoor about their respective rollouts of 625 electric scooters."""

word_cloud = WordCloudGenrator(input_txt=test_txt)

