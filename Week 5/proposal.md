Megan Englert

CISC367 S21

17 March 2021

## Midterm Project - First Milestone Submission

### The Problem

Education inequity has been a long-term issue in the United States. Decades of redlining, a discriminatory practice by mortgage lenders or insurance providers that keep individuals of certain races or income levels out of wealthy areas, have left distinct divides between communities of individuals with different characteristics. The existence of such harshly defined pockets of income, resulting in different amounts of income being available to K-12 schools in the area, has likely caused an inherent advantage to students coming from privileged families.

Furthermore, charter schools continue to be debated in Delaware. Charter schools are significantly more prevalent in Delaware than in other states, and their ethics have long come into question. While it makes sense that parents want to be able to choose their child's education, there are not enough charter schools to meet demand right now. Do parents really get to "choose" when they are reliant on their student's scores or a random lottery to be able to actually make that choice? Many people protest charter schools, however, arguing that the per-student funding lost from public schools makes a difference. A few students per grade leaving results in lost funding in many states, but does not decrease the cost of faculty or maintaining the building.

I plan to explore education inequity in Delaware through test results, including assessments such as the SAT and the Delaware Comprehensive Assessment System (DCAS). I have found data that will allow me to compare results between regular and charter schools, races, and income levels to see if there is a statistically significant difference between scores in any of these categories.

### The Questions

- Do students from charter schools perform statistically significantly better on these assessments than students from non-charter, or "regular," as the dataset calls them, schools?
- Within districts, do students from certain races or income levels perform statistically significantly better than other students within their same district?
- Do districts with a higher proportion of students of certain races or income levels perform statistically significantly better than districts with lower amounts of those students?

### Justification

A 2014 publication by the Economic Policy Institute, [Richard Rothstein's "The Racial Achievement Gap, Segregated Schools, and Segregated Neighborhoods - A Constitutional Insult"](https://www.epi.org/publication/the-racial-achievement-gap-segregated-schools-and-segregated-neighborhoods-a-constitutional-insult/), analyzes the factors of race and income level that play into educational success. Rothstein considers both factors outside the classroom, such as worse health care causing absences, less educated parents, and fewer opportunities for enrichment outside of school, and inside it, like how higher student mobility results in repeated lessons and the requirement for more remediation leaving excelling students left behind. Furthermore, these students' lesser successes in education result in lower expected income, dooming their children to a similar future unless this inequality is resolved.

Rothstein cites statistics found by NYU sociologist Patrick Sharkey in 2013:
> "Sharkey finds that young African Americans (from 13 to 28 years old) are now ten times as likely to live in poor neighborhoods, defined in this way, as young whites—66 percent of African Americans, compared to 6 percent of whites (Sharkey, 2013, p. 27, Fig. 2.1). What’s more, for black families, mobility out of such neighborhoods is much more limited than for whites. Sharkey shows that 67 percent of African American families hailing from the poorest quarter of neighborhoods a generation ago continue to live in such neighborhoods today. But only 40 percent of white families who lived in the poorest quarter of neighborhoods a generation ago still do so (Sharkey, 2013, p. 38, Fig. 2.6)" (Rothstein).

These educational disparities play strongly into the cycle of poverty, especially for non-white students, who often have a more difficult time overcoming their circumstances due to biased employers and educational institutions. 

The choice and opportunity to attend charter schools could similarly impact students' ability to achieve. [Zachary Jason's The Battle Over Charter Schools](https://www.gse.harvard.edu/news/ed/17/05/battle-over-charter-schools), published in Harvard Ed. Magazine in Summer 2017, analyzes both side's thoughts. At the time of writing, 32,000 children, with a majority Black and Latino population, were on waitlists for existing charter schools, seeking access to a better education than a public school could offer (Jason). Not all charter schools are created equal; 200 close each year, sometimes in the middle of a school year or even school day, and one was caught being used as an illegal nightclub on the weekends (Jason). Jason also cites charter schools' high teacher turnover rate, 24 percent, double that of traditional schools, which could potentially stifle student success (Jason). However, if implemented properly, charter schools could help motivated students and families to find a better education.

While charter schools are struggling to pass legislation in some states (Jason), [the National Alliance for Public Charter Schools](https://www.publiccharters.org/our-work/charter-law-database/states/delaware) recorded 16,086 DE charter students in the 2018-2019 school year, accounting for 13% of the total public school enrollment. Furthermore, Delaware is ranked 15th by the NAPCS for its public charter laws, since it "provides a fair amount of autonomy and accountability to its public charter schools, but it provides inequitable funding to charter schools" ("Delaware").

### Datasets

The main dataset I will be using is the [Student Assessment Performance data](https://data.delaware.gov/Education/Student-Assessment-Performance/ms6b-mt82), provided by the Delaware Department of Education. As it does not provide information on which districts are regular vs. charter, I will be using the matching district codes from the [Delaware Public Education Organization Directory](https://data.delaware.gov/Education/Delaware-Public-Education-Organization-Directory/p3ez-si4g), also provided by the Delaware Department of Education, to add that characteristic into my data.

### Ethical Concerns

- **Causation Assumptions**: 
    - **Race and Income Level**: Analysis of this data may show that students of certain races or income levels tend to get better or worse test scores. If analysis is made implying a direct causation, it implies that these students are simply incapable of getting comparable test scores instead of experiencing environmental factors that affect their results. In my analysis, it must be made clear any association found is likely a result of the many explanations offered by Rothstein, such as worse support at home and worse funding.
    - **Charter Schools**: Furthermore, this analysis may also show that students in charter schools tend to perform better or worse than students in traditional schools. This may also be caused by a myriad of factors, especially considering that some charter schools use merit-based admission. They may also be experiencing better educational support at home, since their parents went through the effort to actively change their school. While the data may show that either traditional or charter schooling is better for test scores, it may simply be the factors surrounding who is currently able to access charter schools.
- **Funding**:
    - **Race and Income Level**: Rather than trying to distribute funding so that all can access education equally, some may argue that schools receiving better test scores should continue to get more funding to give their high-achieving students more opportunities to succeed in different areas. Money spent on remediation is not spent on advancement, and a more utilitarian argument may see value in leaving students in the educational dust while others receive even more opportunities.
    - **Charter Schools**: Continuing with the idea of causation, because of the way that charter school students are selected, there may be many outside factors causing a difference in scores. Furthermore, even if they are beneficial, they may not be the one-size-fits-all solution. For example, one cost of charter schools is the variety of programs offered. If 1 in 25 students are interested in playing in a music ensemble or taking a certain specialized course, a 1,000 student public school could easily justify the cost of providing facilities and a teacher. A 200 person charter school, however, would still have to find a teacher and facilities for those 8 students, and they can't simply pay the teacher 1/5 of a salary for teaching 1/5 of the students. The further breakdown of traditional schools into charter schools has likely not been studied well enough to try to successfully implement on a state-wide level.

### Data Considerations

- **Test scores**: The merit of test scores as a measure of education has been argued for a pretty long time, but that is the numerical data that is available. A lot of elements, such as available extracurriculars, student to faculty ratio, etc. that can all play into a student's education and success are not reflected at all here.
- **"REDACTED"**: Unfortunately, some of this data has been redacted to protect information in less represented categories, such as the SAT Essay scores for Homeless 12th Graders at Caesar Rodney School District.
- **Correct Reporting**: While the data provides specified sub-categories for students with disabilities, students experiencing homelessness, students from low-income families, and multi-racial students, we do have to rely on what the school knows about these students or what they reported themselves. Furthermore, the dataset does not actually define what terms like "low income" actually mean.
- **Income Levels**: The data provides "low income" distinctions of students, but not high or medium. This means that we won't be able to compare the low to the high as much as we'll have to compare the low to everyone, including the low.

### Works Cited
"Delaware." *National Alliance for Public Charter Schools*, https://www.publiccharters.org/our-work/charter-law-database/states/delaware. Accessed 17 March 2021.

Jason, Zachary. "The Battle Over Charter Schools." *Harvard Ed. Magazine*, President and Fellows of Harvard College, Summer 2017, https://www.gse.harvard.edu/news/ed/17/05/battle-over-charter-schools. Accessed 17 March 2021.

Rothstein, Richard. "The Racial Achievement Gap, Segregated Schools, and Segregated Neighborhoods - A Constitutional Insult." *Economic Policy Institute*, 12 Nov. 2014, [https://www.epi.org/publication/the-racial-achievement-gap-segregated-schools-and-segregated-neighborhoods-a-constitutional-insult/](https://www.epi.org/publication/the-racial-achievement-gap-segregated-schools-and-segregated-neighborhoods-a-constitutional-insult/). Accessed 17 March 2021.
