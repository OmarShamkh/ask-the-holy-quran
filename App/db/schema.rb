# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2022_07_20_100700) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "ayas", force: :cascade do |t|
    t.text "content"
    t.integer "number"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.text "text"
    t.integer "sura"
    t.integer "indexe"
    t.string "revelation_place"
    t.integer "aya_number"
    t.string "surah_name"
    t.integer "surah_number"
    t.integer "chapter_id"
  end

  create_table "chapters", force: :cascade do |t|
    t.string "revelation_place"
    t.string "name"
    t.integer "chapter_number"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "surahs", force: :cascade do |t|
    t.string "name"
    t.integer "surah_id"
    t.string "place"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "suras", force: :cascade do |t|
    t.integer "number"
    t.string "name"
    t.string "location"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "tafseers", force: :cascade do |t|
    t.string "tafser"
    t.string "ayanumber"
    t.integer "chapter_number"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.integer "aya_number"
    t.string "aya_order"
    t.string "chapter_id"
  end

end
