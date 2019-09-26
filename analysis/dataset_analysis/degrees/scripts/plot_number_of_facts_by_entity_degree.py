import matplotlib.pyplot as plt

from dataset_analysis.degrees import entity_degrees
from dataset_analysis.degrees import relation_mentions
from datasets import FB15K, Dataset, YAGO3_10

from io_utils import *
from collections import defaultdict


def plot_dict(dict, title, xlabel, ylabel):
    x = []
    y = []

    for item in (sorted(dict.items(), key=lambda x: x[0])):
        x.append(item[0])
        y.append(item[1])

    plt.scatter(x, y, s=1, color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    #plt.xscale('log')
    #plt.yscale('log')
    plt.show()


def get_dicts(dataset_name):
    _, _, entity_2_degree = entity_degrees.read(dataset_name)
    relation_2_mentions = relation_mentions.read(dataset_name)
    dataset = Dataset(dataset_name)

    head_degree_2_amount_of_facts = defaultdict(lambda:0)
    tail_degree_2_amount_of_facts = defaultdict(lambda:0)
    relation_mentions_2_amount_of_facts = defaultdict(lambda:0)


    for (head, relation, tail)  in dataset.train_triples:

        head_degree = entity_2_degree[head]
        tail_degree = entity_2_degree[tail]
        rel_mentions = relation_2_mentions[relation]

        head_degree_2_amount_of_facts[head_degree] += 1
        tail_degree_2_amount_of_facts[tail_degree] += 1
        relation_mentions_2_amount_of_facts[rel_mentions] += 1

    return head_degree_2_amount_of_facts, tail_degree_2_amount_of_facts, relation_mentions_2_amount_of_facts


head_degree_2_facts, tail_degree_2_facts, relation_mentions_2_facts = get_dicts(YAGO3_10)

plot_dict(head_degree_2_facts, "head degree vs amount of facts", "head degree", "amount of test facts with heads of that degree")
plot_dict(tail_degree_2_facts, "tail degree vs amount of facts", "tail degree", "amount of test facts with tails of that degree")
plot_dict(relation_mentions_2_facts, "relation mentions vs amount of facts", "relation mentions", "amount of test facts with relations of that mentions")
