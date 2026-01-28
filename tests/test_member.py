from library_system.member import Member

def test_member_fine():
    member = Member("Aravind", "M01")
    member.add_fine(3)
    assert member.fine_amount == 15
