Feature: basic crud operations on a btree

    Scenario: find a node
        Given we have a non empty btree
        When we try to find an element
        Then it returns the element pointer and the node that contains it