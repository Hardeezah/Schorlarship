# Cambridge PhD Outreach Emails

Below are the finalized outreach emails for the two prospective supervisors. Make sure to replace the GitHub repository links if they ever change.

---

## 1. Email to Prof. Nic Lane (CaMLSys Lab)
**Focus:** Federated Edge Learning for Agricultural Vision

**Subject:** Prospective PhD Student (2027) – Federated Edge Learning for Agricultural Vision

Dear Prof. Lane,

I am writing to express my strong interest in joining CaMLSys as a PhD student. I recently graduated with First Class Honours in Computer Science from Ahmadu Bello University (CGPA 4.53/5.00). My applied ML engineering focuses on severe hardware constraints, work which recently won 1st Place globally at the Huawei ICT Innovation Competition Finals (2025, China).

For that competition, I built CropDiseaseDetector, an agricultural vision model deployed entirely offline on an Orange Pi AIpro. Continuously improving it with real-world field data across smallholder farmers presents a structural bottleneck: we cannot reliably transmit gigabytes of crop imagery from rural farms over poor 2G/3G networks to a central server.

I read the Flower paper's evaluation of network heterogeneity, particularly the finding that FL training time varied from under 9 minutes to over 108 minutes depending on simulated real-world client bandwidth, and the FedFS sampling strategy your group proposed to address it. This directly mirrors the constraint I face with CropDiseaseDetector: continuously updating the model with field data from smallholder farmers on 2G/3G connections is exactly the kind of low-bandwidth, heterogeneous-client scenario your framework was built to handle. I am proposing a PhD research direction that extends this work into computer vision for agricultural edge devices: investigating how federated learning (via Flower) can be optimized for constrained, image-based inference in rural deployments, enabling decentralized model updates without moving raw field data.

Given my practical experience deploying offline models, I am deeply interested in tackling the systems-level bottlenecks of edge AI that your lab focuses on. My full project report is available at https://doi.org/10.5281/zenodo.22287430, and the source code is on GitHub: https://github.com/Hardeezah/cdd_electron (Edge App) and https://github.com/Hardeezah/cdd-mobile (Mobile App).

Are you planning to take on new PhD students for the upcoming cycle, and would this applied direction align with your current lab focus?

Thank you for your time,
Hadiza Mohammed
---

## 2. Email to Dr. Ferenc Huszár
**Focus:** Out-of-Distribution Generalization and Dynamic Feature Recognition

**Subject:** Prospective PhD Student (2027) – OOD Generalization and Dynamic Feature Recognition

Dear Dr. Huszár,

I am writing to express my strong interest in joining your lab for my PhD. I recently graduated with First Class Honours in Computer Science from Ahmadu Bello University (CGPA 4.53/5.00). My engineering background focuses on building ML systems for unpredictable environments, work which recently won 1st Place globally at the Huawei ICT Innovation Competition Finals (2025, China).

For that competition, I built CropDiseaseDetector, an agricultural vision model deployed offline on an Orange Pi AIpro. However, in deploying this toward real smallholder farmers, I recognized a critical gap: I lack a rigorous way to measure if model accuracy holds under extreme real-world distribution shifts-such as different camera lenses in the field or varying lighting conditions.

I have been following your work on Out-of-Distribution (OOD) generalization. I found your paper, "Rule Extrapolation in Language Models," particularly compelling in how it rigorously tests rule extrapolation when models encounter data that violates training distributions.

For my PhD, I want to move these theoretical OOD frameworks into constrained visual environments. My proposed research investigates Dynamic Feature Recognition across image sequences as a method to achieve and measure domain generalization, ensuring models don't just memorize training data but extrapolate rules robustly in the field.

My full project report is available at https://doi.org/10.5281/zenodo.22287430, and the source code is on GitHub: https://github.com/Hardeezah/cdd_electron (Edge App) and https://github.com/Hardeezah/cdd-mobile (Mobile App). Are you accepting new students for the upcoming cycle, and does bridging your theoretical OOD work with applied visual environments align with your interests?

Thank you for your time,
Hadiza Mohammed