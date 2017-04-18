schoolstr = "schools = models.school.query.add_column(models.school.instnm).add_column(models.school.city).add_column(models.school.stabbr).add_column(models.school.insturl)"
admissionstr = ".join(models.admissiondata, models.admissiondata.opeid == models.school.opeid).add_column(models.admissiondata.adm_rate).add_column(models.admissiondata.adm_rate_rank).add_column(models.admissiondata.sat_avg).add_column(models.admissiondata.sat_avg_rank)"
collegestr = ".join(models.collegedata, models.collegedata.opeid == models.school.opeid).add_column(models.collegedata.pftfac).add_column(models.collegedata.pftfac_rank).add_column(models.collegedata.locale).add_column(models.collegedata.ugds_white).add_column(models.collegedata.ugds_white_rank).add_column(models.collegedata.inexpfte).add_column(models.collegedata.inexpfte_rank).add_column(models.collegedata.grad_debt_mdn).add_column(models.collegedata.grad_debt_mdn_rank)"
gradstr = ".join(models.graddata, models.graddata.opeid == models.school.opeid).add_column(models.graddata.c150_4).add_column(models.graddata.c150_4_rank)"
orderbystr = ".order_by("
#limitstr = ".limit(25).all()"
limitstr = ".all()"
rankstr = "_rank"
joinstr = schoolstr + admissionstr + collegestr + gradstr

attrs=["models.admissiondata.adm_rate","models.admissiondata.sat_avg",
			"models.collegedata.pftfac", "models.collegedata.ugds_white","models.collegedata.inexpfte","models.collegedata.grad_debt_mdn",
			"models.graddata.c150_4","models.collegedata.locale"]

ranks=["models.admissiondata.adm_rate_rank","models.admissiondata.sat_avg_rank",
			"models.collegedata.pftfac_rank", "models.collegedata.ugds_white_rank","models.collegedata.inexpfte_rank","models.collegedata.grad_debt_mdn_rank",
			"models.graddata.c150_4_rank","models.collegedata.locale_rank"]