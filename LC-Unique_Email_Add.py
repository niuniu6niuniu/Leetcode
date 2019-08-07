# # #     Unique Email Address     # # #

# Every email consists of a local name and a domain name, separated by the @ sign.
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com is
# the domain name.Besides lowercase letters, these emails may contain '.'s or '+'s.

# If you add periods ('.') between some characters in the local name part of an
# email address, mail sent there will be forwarded to the same address without
# dots in the local name. For example, "alice.z@leetcode.com" and
# "alicez@leetcode.com" forward to the same email address.
# (Note that this rule does not apply for domain names.)

# If you add a plus ('+') in the local name, everything after the first plus sign
# will be ignored. This allows certain emails to be filtered,
# for example m.y+name@email.com will be forwarded to my@email.com.
# (Again, this rule does not apply for domain names.)

# It is possible to use both of these rules at the same time.
# Given a list of emails, we send one email to each address in the list.
# How many different addresses actually receive mails?

# Example 1:
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

class Solution:
    def numUniqueEmails(self, emails):

        # # #   Solution 1   # # #
        #  For string before '@': 1. Remove '.' if '.' exists
        #                         2. Remove string after '+'
        #  For string after '@': '.' and '+' are unique
        # editEmail = []
        # for email in emails:
        #     # split email into 2 sub-email based on '@'
        #     subEmail = email.split('@')
        #     # remove '.' in first sub-email
        #     subEmail[0] = subEmail[0].replace('.','')
        #     # remove string after '+'
        #     if subEmail[0].find('+') != -1:
        #         idxPlus = subEmail[0].find('+')
        #         subEmail[0] = subEmail[0][:idxPlus]
        #     email = '@'.join(subEmail)
        #     editEmail.append(email)
        # # delete repeated form
        # Unik = set(editEmail)
        # return len(Unik)

        # # #   Solution 2   # # #
        Unik = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.','')
            Unik.add(local + '@' + domian)
        return len(Unik)

t = Solution()
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(t.numUniqueEmails(emails))
