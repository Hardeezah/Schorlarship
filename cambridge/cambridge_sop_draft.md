# Statement of Purpose
**Name:** Hadiza Mohammed
**Program:** PhD in Computer Science, University of Cambridge
**Scholarship:** Gates Cambridge Scholarship

I am applying to the PhD in Computer Science at the University of Cambridge to build machine learning systems that maintain mathematical guarantees of robustness when deployed outside the curated datasets they are trained on. Specifically, I intend to research federated edge learning and out-of-distribution (OOD) generalization for constrained hardware, focusing on deployments in low-connectivity settings across West Africa where the gap between benchmark accuracy and field performance has direct economic consequences.

**Academic Excellence and Engineering Foundation**
I graduated with First Class Honours in Computer Science from Ahmadu Bello University, achieving a CGPA of 4.53/5.00. However, my academic rigor has always been defined by bridging the gap between theoretical computer science and hardware-constrained engineering. 

During my undergraduate studies, I led the development of *CropDiseaseDetector*, a combined hardware and vision system designed for smallholder farmers. The structural constraint of this domain is that the model must run offline on hardware a rural farmer can own. I trained a MobileNetV2-based classifier and a YOLOv8n detector, applying SMOTE for data balancing, and deployed both models to run entirely offline on an Orange Pi AIpro equipped with a Huawei Ascend chip. The system achieved 98% accuracy on a held-out dataset and integrated a Random Forest model fed by an NPK 7-in-1 soil sensor. For this engineering work, our team won 1st Place globally at the 2025 Huawei ICT Innovation Competition Finals in China, and the soil module placed 2nd in the Nigeria MATLAB Student Coding Challenge.

**The Research Gap: OOD Generalization and Federated Edge Learning**
Despite achieving high accuracy on curated data, my deployment of *CropDiseaseDetector* exposed a critical gap that I am asking a PhD to help me solve. A curated Kaggle dataset does not capture the lighting, occlusion, and camera variation of images a farmer captures in the field. I currently lack a rigorous, theoretical framework to guarantee that my offline models will not silently fail under these extreme distribution shifts. Furthermore, continuously improving the model across thousands of farmers without requiring them to upload gigabytes of images over poor 2G/3G networks requires decentralized training directly on the edge.

Alongside this, my work as a founding engineer at KodaTrade-an AI compliance platform helping Nigerian SMEs navigate cross-border trade-exposed a parallel bottleneck. I built a retrieval-augmented vision model to parse customs documents, but because SME regulatory data is highly sensitive, it cannot be legally centralized for model training. 

**Reasons for Choice of Course (Why Cambridge)**
The University of Cambridge’s Computer Laboratory is the only environment where I can bridge my hardware deployment experience with the rigorous mathematical frameworks needed to solve these bottlenecks. 

Specifically, I am drawn to the Machine Learning Systems Lab (CaMLSys) and the work of Prof. Nic Lane. His foundational work on the Flower framework and federated edge learning provides the exact architecture required to decentralize training across both constrained agricultural edge devices and siloed SME regulatory data. I am equally drawn to the theoretical work of Dr. Ferenc Huszár on probabilistic deep learning. His recent investigations into "rule extrapolation" and compositional generalization on OOD prompts provide the rigorous mathematical framework I need to measure domain generalization. 

My proposed research investigates Dynamic Feature Recognition across image sequences as a method to achieve domain generalization under embedded-device constraints, while utilizing federated learning to aggregate these insights without centralizing raw data. I want to prove that theoretical OOD frameworks can be successfully grounded in constrained agricultural environments.

**Leadership and Commitment to Improving the Lives of Others**
The thread connecting my work-from an offline disease detection device for smallholder farmers to a compliance platform for emerging SMEs-is a commitment to building AI infrastructure that empowers the economically marginalized. When I presented KodaTrade at the UNITAR forum on Japan-Africa public-private partnerships under TICAD9, the clearest consensus was that the barriers to economic formalization in emerging markets are structural. 

Building ML models for these environments is not a purely technical exercise; it is an act of economic enablement. Leadership, to me, has meant taking the initiative to engineer solutions within the constraints of my community, whether that meant leading a student team to a global hardware victory in China or architecting compliance software for local businesses. A PhD at Cambridge, supported by the Gates Cambridge Scholarship, will provide me with the world-class theoretical training necessary to ensure the systems I build for these communities are not just locally functional, but mathematically robust, privacy-preserving, and globally scalable.

---
**References**
[1] CropDiseaseDetector. Huawei ICT Innovation Competition 2024-2025. 1st place, global finals, China (2025). 
[2] Nigeria MATLAB Student Coding Challenge, 2024. 2nd place. Smart soil analysis module.
[3] UNITAR forum, "Empowering Youth and Women amid Economic Instability." Koda presented (participant).
