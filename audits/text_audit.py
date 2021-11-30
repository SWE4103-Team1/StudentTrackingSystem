def generate_text_audit(audit_json):
	"""
	Generates and returns a list of text lines that contains student audit information.
	The JSON data from /audit_student/<student number> is passed as parameter.
	"""
	body = [str(audit_json['target_student']['full_name'])]
	return body