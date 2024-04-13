import gen_utils

row_0 = gen_utils.Row(
    school_name="Brown University",
    gpa=3.5,
    degree=gen_utils.Degree.BACHELORS,
    location="Providence",
    gender=gen_utils.Gender.MALE,
    veteran_status=gen_utils.VeteranStatus.NOT_APPLICABLE,
    work_authorization=gen_utils.WorkAuthorization.YES,
    disability=gen_utils.Disability.NOT_APPLICABLE,
    ethnicity=gen_utils.Ethnicity.WHITE,
    jobs=[gen_utils.Job(), gen_utils.Job(), gen_utils.Job()]
)

gen_utils.generate_csv("test", rows=[row_0], for_candidate_evaluator=False)