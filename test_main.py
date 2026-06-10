from main import check_password_strength, main


def test_short_password():
    assert check_password_strength("123aN") == 3


def test_no_capital_letters():
    assert check_password_strength("abcd1234") == 3


def test_no_numbers_password():
    assert check_password_strength("abSMKOPNKNFk") == 3


def test_no_lower_case_letters():
    assert check_password_strength("NOLOWERCASELETTERS10") == 3


def test_strong_password():
    assert check_password_strength("Strong10#password") == 5


def test_no_special_letters():
    assert check_password_strength("StrongPassword10") == 4


def test_main_super_weak_password(monkeypatch, capsys):
    monkeypatch.setattr("getpass.getpass", lambda _: "")
    main()
    captured = capsys.readouterr()

    assert "Welcome to Password-Checker!" in captured.out
    assert "Strength Level: Super Weak 🥶" in captured.out


def test_main_very_weak_password(monkeypatch, capsys):
    monkeypatch.setattr("getpass.getpass", lambda _: "1")
    main()
    captured = capsys.readouterr()

    assert "Welcome to Password-Checker!" in captured.out
    assert "Strength Level: Very Weak ⚠️" in captured.out


def test_main_weak_password(monkeypatch, capsys):
    monkeypatch.setattr("getpass.getpass", lambda _: "1a")
    main()
    captured = capsys.readouterr()

    assert "Welcome to Password-Checker!" in captured.out
    assert "Strength Level: Weak 👎🏽" in captured.out


def test_main_medium_password(monkeypatch, capsys):
    monkeypatch.setattr("getpass.getpass", lambda _: "1aB")
    main()
    captured = capsys.readouterr()

    assert "Welcome to Password-Checker!" in captured.out
    assert "Strength Level: Medium 👍🏽" in captured.out


def test_main_strong_password(monkeypatch, capsys):
    monkeypatch.setattr("getpass.getpass", lambda _: "1234AbCdEfG")
    main()
    captured = capsys.readouterr()

    assert "Welcome to Password-Checker!" in captured.out
    assert "Strength Level: Strong 💪🏽" in captured.out


def test_main_very_strong_password(monkeypatch, capsys):
    monkeypatch.setattr("getpass.getpass", lambda _: "1234@AbCdEfG")
    main()
    captured = capsys.readouterr()

    assert "Welcome to Password-Checker!" in captured.out
    assert "Strength Level: Very Strong 🔥" in captured.out
