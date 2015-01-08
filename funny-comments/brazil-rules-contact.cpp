// 
// Funny Comment :)
// 
//	

/*
The rules of physical contact have a considerable variability all around the World.

In Brazil, they are not trivial, so I created this OOP algorithm when I was in college:
*/

void Brazil::PhysicalContactRule (Person p, Person q)
{
	if ((p.gender == q.gender) && p.gender == gender::male) {
		p.handshakes(q);
	} else {
		if (location == “Rio de Janeiro”) {
			p.kiss_on_the_cheek (q);
			q.kiss_on_oposite_cheek (p); // check documentation
		} else {
			p.kiss_on_the_cheek_while_being_simultaneusly_kissed (q);
		}
	}
}

/*
I have studied all my life in a boys-only private school where we followed this rule but we didn’t have the trouble to learn the second part (also the p.handshakes(q) could be replaced by p.punches_on_the_arm(q); q.punches_on_the_arm(p)

When we entered college things got complicated. During some classes a girl, I never met before would get close and perform her part of the algorithm, and that created funny situations. Also, I feared that this kissing issue was too much “improper” and began to offer a hand when a girl approached to execute the greet algorithm. Some girls got the clue, and we shake hands, others completely ignored the extended hand and invaded my airspace to kiss on the cheek.

Eventually, I adopted the whatever attitude, if you want to kiss, do it, if you accept my extended hand that's ok too.

But then I moved to another state and the third part of the algorithm kicked in which lead to other funny situations.

When my job required me to travel to many countries I began to notice and appreciate the distinct shades that regulate physical contact and greeting: a Priest handshaking you at the end of the Mass in some countries, an elder man who kissed me on the cheek in Italy and thank God I never been in Moscow to experience the old “Socialist fraternal kiss” :).

Some countries definitely let people fell less lonely than others.
*/
