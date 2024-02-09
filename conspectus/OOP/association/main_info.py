"""
Simple imitation in OOP allows a class to imitate the behavior and properties 
of another class. Although this is a powerful tool for avoiding code duplication, 
it has some limitations. Inheritance creates a close dependency between a base class 
and derived classes. Changes to the base class can unexpectedly affect the behavior 
of derived classes. Inheritance can lead to inheriting methods that don't make sense 
for the derived class, which can lead to unexpected or erroneous behavior.

Association offers an alternative to imitation that can avoid some of its drawbacks. 
Association in OOP is a concept that describes the relationship between classes through their objects. 
In this context, a class can include another class as one of its fields described by the word "has".

Association is divided into two main types: composition and aggregation, 
each of which has its own characteristics and applications.

The main difference between composition and aggregation is the degree of dependence 
of the "parts" on the "whole". In a composition, the "parts" are so dependent on the "whole" 
that they cannot exist without it, while in an aggregation, the "parts" have greater 
independence and can exist separately from the "whole." The choice between these two types 
of relationships depends on the specific situation and how strong or weak the relationship 
between the objects in your class model should be.
"""
