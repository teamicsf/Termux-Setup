# ===============================================================================
# ⚠️  CAUTION / WARNING
# --------------------------------------------------------------------------------------------------
# This program is created for educational, testing, and research purposes only.
# The developer is not responsible for any misuse, illegal activity, or damage caused by this code.
#
# If you are using this script, make sure you have proper authorization and permission
# before running it on any system, server, network, or website.
#
# Unauthorized testing, scanning, or attacking systems without permission may violate
# cybersecurity laws and could lead to serious legal consequences.
#
# Always use this tool responsibly, ethically, and only in controlled environments
# such as your own lab, test server, or systems where you have full permission.
#
# By running this program you agree that you understand the risks and you take full
# responsibility for how this code is used.
# --------------------------------------------------------------------------------------------------
# Developed for learning, experimentation, and ethical cybersecurity practice.
# ==================================================================================================
import base64,zlib,marshal
# Another silent line inside the script
# Code is calm but powerful
# A random idea turned into logic
# Every coder started with hello world
# This script has a small piece of imagination
# The keyboard is the coder's sword
# Logic written line by line
# Somewhere a future project begins here
# A tiny thought left in the code
# Keep exploring new possibilities
# Code written with curiosity
# Just another peaceful line of comment
# A place where ideas meet syntax
# Simple code can change big things
# The developer brain never sleeps
# Quiet code doing loud work
# Hidden creativity in this file
# One more thought before the next function
# Programming is controlled chaos
# Every script has a story
# Code is just structured thinking
# A comment passing through the file
# Let the logic flow naturally
# Another tiny mark of a developer
# Curiosity creates great programs
# Code today, knowledge forever
# Silent observer inside the program
# Just a friendly line of comment
# Lines like this make code human
# Another calm moment in the script
# A pause before the next algorithm
# Programmer thoughts written quietly
# Even comments have their own life
# Code slowly becoming something bigger
# A random developer left this here
# Logic grows with every line
# The script continues its journey
# Ideas converted into instructions
# Coding is thinking in structure
# A little creativity inside the file
# Just another mysterious line inside the code
# Silence of the code, power of the logic
# A developer was here
# Writing code like painting with logic
# This line does nothing but looks cool
# Code running somewhere in the universe
# Late night coding session continues
# Turning coffee into Python scripts
# Another day, another script
# Somewhere a bug is hiding
# Searching for the perfect algorithm
# A small comment with big dreams
# Lines of code building the future
# Sometimes code works like magic
# Never stop learning new things
# Code smarter, not harder
# Even comments can have personality
# Logic is the language of machines
# A silent guardian inside the script
# Developer mode always on
# Code flowing like a river
# Keep pushing the limits
# Hidden creativity inside this file
# One more line for style
# Clean code feels satisfying
# If you read this, you're curious
# Another random thought in the script
# Code today, innovation tomorrow
# Quiet lines but powerful ideas
# End of another set of random comments
data = "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"

code = marshal.loads(zlib.decompress(base64.b64decode(data)))
# Always take time to understand the logic behind the code instead of only copying it from somewhere else.
# A good developer learns not only how a program works but also why it works that way.
# Before running any powerful script, always make sure you fully understand what it is doing internally.
# Never run unknown code on your system without reading it carefully and checking its behavior.
# Always test your scripts in a safe environment before using them in any real situation.
# Remember that patience is one of the most important skills a programmer can develop.
# If your code fails today, treat it as a lesson that will make you a better developer tomorrow.
# Writing clean and understandable code will help both you and others in the future.
# Never rush when debugging because small mistakes often hide in simple places.
# Always keep learning new concepts because technology changes faster than we expect.
# Try to write programs that are simple and clear rather than complicated and confusing.
# Understanding a small piece of logic deeply is more valuable than knowing many things superficially.
# Good programmers spend more time thinking about problems than typing code.
# Every bug you solve improves your ability to think logically.
# Always organize your code so that future updates become easier to manage.
# Learning programming is a journey that requires curiosity and persistence.
# Never feel discouraged by errors because they are a natural part of development.
# The more you experiment with code, the more confident you will become.
# A responsible developer always considers the ethical impact of the tools they create.
# Always respect privacy and security when working with any kind of data.
# Avoid writing code that could harm systems or violate trust.
# A strong developer focuses on learning rather than showing off.
# Always document your scripts so that others can understand their purpose.
# If something works today, still review it later to see if it can be improved.
# Try to keep your code efficient so it runs smoothly even on weaker devices.
# Always remember that knowledge grows step by step through practice.
# Reading other people's code can teach you many useful techniques.
# Never stop asking questions when you don't understand something.
# Learning cybersecurity also means learning responsibility and ethics.
# Always use powerful tools only in environments where you have permission.
# A calm mind often finds solutions faster than a stressed one.
# Coding late at night sometimes brings creative solutions to difficult problems.
# Simple scripts often become the foundation of bigger projects.
# Always keep backups of important code so your work is never lost.
# Clean structure in a program saves hours of confusion later.
# Avoid unnecessary complexity because clarity makes code stronger.
# Great developers are always humble enough to keep learning.
# Practice writing small projects regularly to strengthen your skills.
# Try to understand errors instead of ignoring them.
# Sometimes stepping away from the screen helps you see the problem clearly.
# A thoughtful developer values quality more than speed.
# Always check your code twice before sharing it with others.
# Programming is not only technical work but also creative thinking.
# Build tools that solve real problems rather than creating confusion.
# Keep improving your knowledge of algorithms and logical thinking.
# A good script should be easy for another developer to read and maintain.
# Respect the systems you test and never misuse technical knowledge.
# Learning slowly but consistently is the best path to mastery.
# Always keep curiosity alive because it is the real engine of innovation.
# Remember that every expert programmer once started as a beginner.
exec(code, globals())
