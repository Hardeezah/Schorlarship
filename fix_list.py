import re

with open('top_20_global_phd_programs.md', 'r') as f:
    content = f.read()

# Delete KAUST
kaust_pattern = r'1\. \*\*KAUST.*?Direct Entry:\*\* Yes\.\n\n'
content = re.sub(kaust_pattern, '', content, flags=re.DOTALL)

# Add UC Berkeley to Tier 3 (at the end)
berkeley_text = """20. **University of California, Berkeley (UC Berkeley, USA)**
    - **Why Apply:** A public Ivy and arguably the top public university globally for Computer Science. Elite AI research through BAIR (Berkeley Artificial Intelligence Research). Fully funded.
    - **Direct Entry:** Yes."""

content = content + "\n" + berkeley_text + "\n"

# Now renumber the list correctly 1 to 20
lines = content.split('\n')
counter = 1
for i, line in enumerate(lines):
    if re.match(r'^\d+\.\s\*\*', line):
        lines[i] = re.sub(r'^\d+\.', str(counter) + '.', line)
        counter += 1

with open('top_20_global_phd_programs.md', 'w') as f:
    f.write('\n'.join(lines))
