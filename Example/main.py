from pywordcloud import WordCloudGenrator

test_txt = """Every enterprise needs to innovate. It doesn’t matter whether you’re are a profit-seeking business, a nonprofit organization, or a government entity. The simple truth is that every business model fails eventually, because conditions change over time. We have to manage not for stability, but for disruption — that, or face irrelevance.

There is no shortage of advice on how to go about it. In fact, there is far too much advice. Design thinkers will tell you to focus on the end user, but Harvard’s Clayton Christensen says that listening to customers too much is how good businesses fail. Then there’s open innovation, lean startups, and on and on it goes.

The truth is that there is no one path to innovation. Everybody has to find their own way. Just because someone had success with one strategy doesn’t mean it’s right for the problem you need to solve. So the best advice is to gather as many tools for your toolbox as you can.

Here are four facts about innovation that you’ll rarely hear, though they’re critically important.

1. Your Success Often Works Against You
For the most part, managers aren’t responsible for innovation. As the title implies, they’re responsible for managing operations. That involves hiring and empowering strong employees, optimizing practices and processes, and reducing errors and mistakes. Managers aren’t generally trying to build a better mousetrap; they’re trying to run things smoothly and efficiently.

It’s easy for someone to stand up on stage at a conference and paint operational managers as dimwits with their heads in the sand. But managing a quality operation is a tough job that requires talent, dedication, and skill. So unless you’ve actually done the job, don’t be too quick to judge.

However, managers do need to realize that there is a fundamental trade-off between innovating and optimizing operations. Running efficient operations requires standardization and control to yield predictable outcomes. Innovation, on the other hand requires experimentation. It means trying a lot of new things, most of which are going to fail.

That’s why success so often leads to failure. What makes you successful in one competitive environment will likely be a hindrance when things change. So you need to find a healthy balance between squeezing everything you can out of the present, while still leaving room to create and build for the future.

2. Look For A Hair-On-Fire Use Case
Good operational managers learn to identify large addressable markets. Bigger markets help you scale your business, drive revenues, and allow you invest back into operations to create more efficiency. Greater efficiencies lead to fatter profit margins, which allow you to invest even more in improvements, creating a virtuous cycle.

Yet, when you’re trying to do something truly new and different, trying to scale too fast can kill your business before it’s even gotten started. A truly revolutionary product is unpredictable because, by its very nature, it’s not well understood. Charging boldly into the unknown is a sure way to run into unanticipated problems that are expensive to fix at scale.

Innovation is never a single event. It is a long process of discovery, engineering, and transformation.
A better strategy is to identify a hair-on-fire use case — someone who needs a problem fixed so badly that they are willing to overlook the inevitable glitches. They will help you identify shortcomings early and correct them. Once you get things ironed out, you can begin to scale for more ordinary use cases.

For example, developing a self-driving car is a risky proposition with a dizzying amount of variables you can’t account for. However, a remote mine in Western Australia, where drivers are scarce and traffic nonexistent, is an ideal place to test and improve the technology. In a similar vein, Google Glass failed utterly as a mass product, but is getting a second life as an industrial tool. Sometimes it’s better to build for the few than the many.

3. Start With the Monkey
When I work with executives, they often have a breakthrough idea that excites them. They begin to tell me what a great opportunity it is and how they are perfectly positioned to capitalize on it. However, when I dig deeper, there’s always a major barrier to making it happen. When I ask about that, they shut down.

Make no mistake. Innovation isn’t about ideas, it’s about solving problems. The truth is that nobody cares about your ideas, they care about the problems you can solve for them. The reason most people can’t innovate isn’t because they don’t have ideas, but because they lack the perseverance needed to stick with a really tough problem until it’s cracked.

At Google X, the tech giant’s “moonshot factory,” the mantra is #MonkeyFirst. The idea is that if you want to get a monkey to recite Shakespeare on a pedestal, you start by training the monkey, not building the pedestal. Because training the monkey is the hard part. Anyone can build a pedestal.

The problem is that most people start with the pedestal, because it’s what they know. And by building it, they can show early progress against a timeline. Unfortunately, building a pedestal gets you nowhere. Unless you can actually train the monkey, working on the pedestal is wasted effort.

4. Sometimes the World Isn’t Ready Yet
When Alexander Fleming first published his discovery of penicillin, no one really noticed. When Xerox executives first got a look at the Alto — the machine that would become the model for the Macintosh seven years later — they didn’t see what the big deal was. When Jim Allison first showed pharmaceutical executives his idea for cancer immunotherapy, not one would invest in it.

We always think the next big thing will be obvious, but in truth, it often starts out looking like nothing at all. When something truly has the power to change the world, the world isn’t ready for it. It needs to build advocacy, gain traction among a particular industry or field, and combine with other innovations before it can make an impact.

But no one ever tells you that. We’re conditioned to think that someone like Steve Jobs or Elon Musk stands up on stage, announces that the world has changed, and everybody just goes along. It never really happens that way because innovation is never a single event. It is a long process of discovery, engineering, and transformation that usually takes about 30 years.

“Don’t worry about people stealing your ideas,” said the computing pioneer Howard Aiken. “If your ideas are any good, you’ll have to ram them down people’s throats.” Never were truer words spoken. Great innovators aren’t just people with ideas. They’re people willing to stick it out and take the shots from people who ridicule them. Eventually, if they’re lucky, they really do change the world.

"""

word_cloud = WordCloudGenrator(input_txt=test_txt)

