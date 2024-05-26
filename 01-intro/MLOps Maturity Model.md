[Machine Learning operations maturity model developped by Microsoft](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model)

**1. No MLOps**
   - No Automation
   - All code in Jupyter notebook
   - DS work alone and they handover the jupyter notebook to the engineers
   - Good for POC and experimentation

**2. DevOps but No MLOps**
  - Engineers are involved and there's some automation involved
  - Automated releases
  - Unit tests, integrations tests
  - CI/CD
  - Ops metrics (network saturation etc.)
  - These systems have the software engineering best practices but they're not ml aware and not specific to ml.
  - No experiment tracking and hard to reproduce the model
  - DS are still separated from the engineering team
  - This maturity level is good when goind from POC to production

**3. Automated Training**
  - Training pipeline
  - Experiment tracking --> You know which models are in production and which are not
  - Model registty
  - Low friction deployment
  - DS and engineers work together
  - This maturity level is good when you have multiple of models are in production and it makes sens to invest in having this kind of infrastructure to make it easier to have training pipelines, track experiments and model registry.

**4. Automated Deployment**
  - Easy to deploy with no human or super low friction
  - Ml Platform has capability to run A/B tests to compare multiple model versions
  - Model monitoring
  - More mature use cases are required to go into this maturity.

**5. Full MLOps Automation**
  - Automated training, automated retraining and automated deployment
  - Automatically tested
  - No human check is required but can be dangerous. 
