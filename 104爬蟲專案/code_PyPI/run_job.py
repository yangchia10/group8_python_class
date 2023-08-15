from findJobs.FindJobs import Jobs

a = Jobs("數據分析師")
a.search_links(max_pages=-1)

a.find_jobs()
a.save_jobs()