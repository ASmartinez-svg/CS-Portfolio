Annex C: Code Quality Assessment Worksheet

Section: 9-Arayat  
Name: Angela Martinez, Zakiyyah Munnilakath, Aurasia Olaso
Date: August 16, 2026  

The problem: Finding the highest (Maximum) number from a list.

---

### 1. Efficiency
**Which algorithm is faster when the list of numbers is very large? Why?**

PseudoCode 1 is faster because it only checks the list one time. PseudoCode 2 has a loop inside another loop, so it repeats a lot of extra work and gets really slow when the list consists of unnecessary elements.

**Checklist:**
* **PseudoCode 1:**
  - Does the algorithm use one loop or two nested loops?: **YES**
  - Does the algorithm repeat work unnecessarily: **NO**
  - Finishes in fewer steps: **YES**

* **PseudoCode 2:**
  - Does the algorithm use one loop or two nested loops?: **YES** (uses 2 nested loops)
  - Does the algorithm repeat work unnecessarily?: **YES** 
  - Finishes in fewer steps: **NO**

---

### 2. Readability
**Which algorithm is easier to understand at first glance? What makes it clearer?**

PseudoCode 1 is easier to understand at first glance because it uses meaningful variable names and has simple logic. It also has fewer lines of code, making it clearer and easier to follow.
   

**Checklist:**
* **PseudoCode 1:**
  - Are variable names meaningful (e.g., max vs. bigger)? **YES**
  - Is the logic simple or complicated? **YES (Simple)**
  - Are there fewer lines of code? **YES**

* **PseudoCode 2:**
  - Are variable names meaningful (e.g., max vs. bigger)? **NO**
  - Is the logic simple or complicated? **NO (Complicated)**
  - Are there fewer lines of code? **NO**

---

### 3. Maintainability
**If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?**

PseudoCode 1 would be easier to update because its structure is straightforward. If we wanted to pass a new feature, such as finding both the maximum and minimum numbers, it would be easier to make changes without causing errors.
   

**Checklist:**
* **PseudoCode 1:**
  - Is the structure straightforward? **YES**
  - Would adding new steps break the code easily? **NO**
  - Is there less chance of errors when updating? **YES**

* **PseudoCode 2:**
  - Is the structure straightforward? **NO**
  - Would adding new steps break the code easily? **YES**
  - Is there less chance of errors when updating? **NO**


---

### 4. Testability
**Which algorithm is easier to test with different inputs? Why?**
   
PseudoCode 1 is easier to test with different inputs because it has simpler logic and fewer conditions to check. It is easy to test with small or large lists, and the output is predictable and clear.



**Checklist:**
* **PseudoCode 1:**
  - Can you test with small lists easily? **YES**
  - Does the algorithm have fewer conditions to check? **YES**
  - Is the output predictable and clear? **YES**

* **PseudoCode 2:**
  - Can you test with small lists easily? **NO**
  - Does the algorithm have fewer conditions to check? **NO**
  - Is the output predictable and clear? **NO**

---

### 5. Security
**Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?**

The algorithm should check if the list is empty and make sure that all inputs are valid numbers. It should also handle unusual or individual inputs properly to prevent errors or crashes.


**Checklist:**
* **PseudoCode 1:**
  - Does the algorithm check if the list is empty? **NO**
  - Does it handle invalid inputs (like letters instead of numbers)? **NO**
  - Does it avoid crashing when inputs are unusual? **NO**

* **PseudoCode 2:**
  - Does the algorithm check if the list is empty? **NO**
  - Does it handle invalid inputs (like letters instead of numbers)? **NO**
  - Does it avoid crashing when inputs are unusual? **NO**

---

6. Final Answer
Which one is the better algorithm and why?

PseudoCode 1 is the better algorithm. It is considerably quicker, shorter, and easier to understand. Unlike PseudoCode 2, it finds the highest number faster without doing unnecessary steps like Pseudocode 2.

