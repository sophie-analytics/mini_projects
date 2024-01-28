class Rule:
    def __init__(self, rule_name: str, rule: str):
        self.rule_name = rule_name
        self.rule = rule

    def set_rule(self, rule: str):
        self.rule = rule

    def get_rule(self):
        return self.rule
    
    def get_rule_name(self):
        return self.rule_name
    
    def set_rule_name(self, rule_name):
        self.rule_name = rule_name
