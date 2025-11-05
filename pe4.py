import wikipedia
import time
import concurrent.futures

#### Section A ####

results = wikipedia.search('Generative artificial intelligence')

#Start time
t1 = time.perf_counter()

for page in results:
    page = wikipedia.page(page, auto_suggest=False)
    title = page.title
    references = page.references
    with open(title+".txt", 'w') as f:
        f.writelines([reference+'\n' for reference in references])
#End time
t2 = time.perf_counter()

print('Using a `for` loop:')
print(t2 - t1)

#### Section B ####

def wiki_dl_and_save(topic):
    """
    input: topic (the name of an article from wikipedia.org as a text string)
    output: write a list of the article's external references to a .txt file
    *the `wiki_dl_and_save` function does not `return` anything
    """
    page = wikipedia.page(topic, auto_suggest=False)
    title = page.title
    references = page.references
    with open(title+".txt", 'w') as f:
        f.writelines([reference+'\n' for reference in references])

results = wikipedia.search('Generative artificial intelligence')

#Start time
t1 = time.perf_counter()

#Context management to make sure to close out properly:
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(wiki_dl_and_save, results)
    executor.shutdown(wait=True)

#End time    
t2 = time.perf_counter()

print('Using `concurrent.futures`:')
print(t2 - t1)