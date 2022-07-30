require "application_system_test_case"

class AyasTest < ApplicationSystemTestCase
  setup do
    @aya = ayas(:one)
  end

  test "visiting the index" do
    visit ayas_url
    assert_selector "h1", text: "Ayas"
  end

  test "creating a Aya" do
    visit ayas_url
    click_on "New Aya"

    fill_in "Content", with: @aya.content
    fill_in "Number", with: @aya.number
    click_on "Create Aya"

    assert_text "Aya was successfully created"
    click_on "Back"
  end

  test "updating a Aya" do
    visit ayas_url
    click_on "Edit", match: :first

    fill_in "Content", with: @aya.content
    fill_in "Number", with: @aya.number
    click_on "Update Aya"

    assert_text "Aya was successfully updated"
    click_on "Back"
  end

  test "destroying a Aya" do
    visit ayas_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Aya was successfully destroyed"
  end
end
